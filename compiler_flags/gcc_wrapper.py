from subprocess import Popen, PIPE, STDOUT
from itertools import combinations
from typing import Callable
import os
import re
import argparse

GCC_BIN = "/usr/bin/g++"

GCC_O1_FLAGS = [
                "-fauto-inc-dec",
                "-fbranch-count-reg ",
                "-fcombine-stack-adjustments",
                "-fcompare-elim",
                "-fcprop-registers",
                "-fdce",
                "-fdefer-pop",
                "-fdelayed-branch",
                "-fdse",
                "-fforward-propagate",
                "-fguess-branch-probability",
                "-fif-conversion",
                "-fif-conversion2",
                "-finline-functions-called-once",
                "-fipa-modref",
                "-fipa-profile",
                "-fipa-pure-const",
                "-fipa-reference",
                "-fipa-reference-addressable",
                "-fmerge-constants",
                "-fmove-loop-invariants",
                "-fmove-loop-stores",
                "-fomit-frame-pointer",
                "-freorder-blocks",
                "-fshrink-wrap",
                "-fshrink-wrap-separate",
                "-fsplit-wide-types",
                "-fssa-backprop",
                "-fssa-phiopt",
                "-ftree-bit-ccp",
                "-ftree-ccp",
                "-ftree-ch",
                "-ftree-coalesce-vars",
                "-ftree-copy-prop",
                "-ftree-dce",
                "-ftree-dominator-opts",
                "-ftree-dse",
                "-ftree-forwprop",
                "-ftree-fre",
                "-ftree-phiprop",
                "-ftree-pta",
                "-ftree-scev-cprop",
                "-ftree-sink",
                "-ftree-slsr",
                "-ftree-sra",
                "-ftree-ter",
                "-funit-at-a-time"]

GCC_O2_FLAGS = [
                "-falign-functions",
                "-falign-jumps",
                "-falign-labels",
                "-falign-loops",
                "-fcaller-saves",
                "-fcode-hoisting",
                "-fcrossjumping",
                "-fcse-follow-jumps",
                "-fcse-skip-blocks",
                "-fdelete-null-pointer-checks",
                "-fdevirtualize",
                "-fdevirtualize-speculatively",
                "-fexpensive-optimizations",
                "-ffinite-loops",
                "-fgcse",
                "-fgcse-lm",
                "-fhoist-adjacent-loads",
                "-finline-functions",
                "-finline-small-functions",
                "-findirect-inlining",
                "-fipa-bit-cp",
                "-fipa-cp",
                "-fipa-icf",
                "-fipa-ra",
                "-fipa-sra",
                "-fipa-vrp",
                "-fisolate-erroneous-paths-dereference",
                "-flra-remat",
                "-foptimize-sibling-calls",
                "-foptimize-strlen",
                "-fpartial-inlining",
                "-fpeephole2",
                "-freorder-blocks-algorithm=stc",
                "-freorder-blocks-and-partition",
                "-freorder-functions",
                "-frerun-cse-after-loop",
                "-fschedule-insns",
                "-fschedule-insns2",
                "-fsched-interblock",
                "-fsched-spec",
                "-fstore-merging",
                "-fstrict-aliasing",
                "-fthread-jumps",
                "-ftree-builtin-call-dce",
                "-ftree-loop-vectorize",
                "-ftree-pre",
                "-ftree-slp-vectorize",
                "-ftree-switch-conversion",
                "-ftree-tail-merge",
                "-ftree-vrp",
                "-fvect-cost-model=very-cheap"
]

GCC_O3_FLAGS = [
                "-fgcse-after-reload",
                "-fipa-cp-clone",
                "-floop-interchange",
                "-floop-unroll-and-jam",
                "-fpeel-loops",
                "-fpredictive-commoning",
                "-fsplit-loops",
                "-fsplit-paths",
                "-ftree-loop-distribution",
                "-ftree-partial-pre",
                "-funswitch-loops",
                "-fvect-cost-model=dynamic",
                "-fversion-loops-for-strides"
        ]

GCC_FLAGS = [GCC_O1_FLAGS, GCC_O2_FLAGS, GCC_O3_FLAGS]


def power_set(s):
    """
    yields a power set
    """
    n = len(s)

    yield ()
    for r in range(1, n+1):
        for combo in combinations(s, r):
            yield combo


def rebuild(target: str, dir: str, optimisations: str, CFLAGS=""):
    """
    rebuild either a 'Make' project
    """

    # first clear the target
    p = Popen(["make", "clean"], stdout=PIPE, stderr=STDOUT, cwd=dir)
    p.wait()

    cmd = ["make", "C_FLAGS = " + CFLAGS + optimisations, target, "-j1"]
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True,
            cwd=dir)

    p.wait()
    assert p.stdout
    if p.returncode != 0:
        print("ERROR Build", p.returncode, p.stdout.read().decode("utf-8"))

    data = p.stdout.readlines()
    data = [str(a).replace("b'", "")
                  .replace("\\n'", "")
                  .lstrip() for a in data]
    return p.returncode, data


def gcc_execute_command(flag: str):
    """ TODO description
    :param flag:
    :return:
    """
    p = Popen([GCC_BIN, flag], stdout=PIPE)
    p.wait()
    assert p.stdout
    output = p.stdout.readlines()

    # the first replace, removes b' from each string
    # the second removes all the unecessery \\b
    # and the last lstrip removes leading whitespaces.
    return [str(a).replace("b'", "")
            .replace("\\n'", "")
            .lstrip() for a in output]


def get_gcc_optimizer_stuff_descriptions(opt):
    """
    opt =
        "--help=optimizer"
        "--help=params"
    """
    if opt not in ["optimizer", "params"]:
        return []

    commands = gcc_execute_command("--help=" + opt)

    # this split() reduces multiple whitespaces to one
    list = [' '.join(a.split()) for a in commands[1:]]

    # this splits every string into two parts on the first whitespace
    cmd_info = [a.split(" ", 1) for a in list]
    return cmd_info


def get_gcc_optimizer_flags():
    """
    return ["--bla1", "--bla2"], [[], 0, [all, None]]

    """
    list = get_gcc_optimizer_stuff_descriptions("optimizer")
    flags = [a[0] for a in list]
    parameters = []
    for i, flag in enumerate(flags):
        pos = flag.find("=")
        if pos != -1:
            # clean the actual flag
            flags[i] = flag[:pos]

            # did we alread reched the end?
            if pos == len(flag) - 1:
                parameters.append([])
                continue

            params = flag[pos+1:]
            # print(params, flag)

            # the optimisation parameter is classified via a number
            if params[0] == "<":
                parameters.append(0)
                continue

            # the only possibility left are options
            assert(params[0] == "[")
            params = params[1:-1]
            parameters.append(params.split("|"))
        else:
            parameters.append([])

    # return [[flags[i], parameters[i]] for i in range(len(flags))]
    return flags, parameters


def get_gcc_params_flags():
    """
    TODO params range return
    """
    list = get_gcc_optimizer_stuff_descriptions("params")
    return [a[0] for a in list]


def get_gcc_diffs(level: int):
    """
    returns the optimisations flags which are available but not activated for
    the fiven `-O{level}` flag
    """
    assert(level < 4)

    not_in_list = []
    not_in_list_j = []
    list, parameters = get_gcc_optimizer_flags()
    docs = get_gcc_optimizer_stuff_descriptions("optimizer")
    for j, valid_flag in enumerate(list):
        found = False
        for c_flag_list in GCC_FLAGS[:level]:
            if valid_flag in c_flag_list:
                found = True
                break

        if not found:
            not_in_list.append(valid_flag)
            not_in_list_j.append(j)

    for i in range(len(not_in_list)):
        j = not_in_list_j[i]
        print(docs[j], parameters[j])


def run(target: str, dir: str, optimisations: str, set_of_flags,
        parse: Callable):

    timings = []
    for flags in power_set(set_of_flags):
        cmd_flags = " ".join(flags) + " "
        print("Flags: ", cmd_flags)
        returncode, data = rebuild(target, dir, optimisations, cmd_flags)
        if returncode != 0:
            print("ERROR build data", data)
            return

        cmd = ["./" + target]
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT,
                  preexec_fn=os.setsid, cwd=dir)
        p.wait()

        if p.returncode != 0:
            print("ERROR RUN: ", p.stdout.read())
            continue
        data = p.stdout.readlines()
        data = [str(a).replace("b'", "")
                      .replace("\\n'", "")
                      .lstrip() for a in data]
        time = parse(data)
        timings.append(time)

    print(timings)


def test_parse(lines: list[str]):
    if len(lines) == 0:
        return 0.0

    lastline = lines[-1]
    matches = re.findall("([+-]?([0-9]*[.])?[0-9]+)", lastline)
    # print(matches)
    if len(matches) == 0:
        return 0.0
    return matches[0][0]


def main():
    parser = argparse.ArgumentParser(description="gcc/clang optimal parameter"
                                     "finder")
    parser.add_argument('--compiler', required=False, type=str,
                        default="/usr/bin/gcc",
                        help="set the path to the compiler ")
    parser.add_argument('--path', required=True, type=str,
                        help="project to optimize.")
    parser.add_argument('--target', required=True, type=str,
                        help="target name: either make or cmake target")
    parser.add_argument('--baseflags', required=False, type=str,
                        help="Baseline flags which are used in each"
                        "optimisation, comma seperated")
    parser.add_argument('--flags', required=False, type=str,
                        help="Flags which are enumerated to find the be"
                        "iterated")
    parser.add_argument('--regex', required=True, type=str, help="regex"
                        "to apply to the ouput to get the optimisation param")
    args = parser.parse_args()

    def parse(lines: list[str]):
        if len(lines) == 0:
            return 0.0

        lastline = lines[-1]
        matches = re.findall(args.regex, lastline)
        print(matches)
        if len(matches) == 0:
            return 0.0
        return matches[0][0]

    try:
        flags = args.flags.split(",")
    except:
        flags = []

    try:
        baseflags = " ".join(args.baseflags.split("."))
    except:
        baseflags = ""

    print(baseflags)
    print(flags)
    run(args.target, args.path, baseflags, flags, parse)


if __name__ == "__main__":
    main()
