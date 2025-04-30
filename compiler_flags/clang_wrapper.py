from subprocess import Popen, PIPE
import logging


CLANG_BIN = "/usr/bin/clang++"
OPT_BIN = "/usr/bin/opt"


def execute_command(flag: str, binary=CLANG_BIN):
    """
    executes any clang command and returns the stdout as a list line by line.
    """
    logging.debug(binary, flag)
    p = Popen([binary, flag], stdout=PIPE)
    output = p.stdout.readlines()

    # the first replace, removes b' from each string
    # the second removes all the unecessery \\b
    # and the last lstrip removes leading whitespaces.
    return [str(a).replace("b'", "")
            .replace("\\n'", "")
            .lstrip() for a in output]


def get_clang_flags():
    """
    return the list of all flags clangs has to offer:
    GOAL:
        ["--bla1", "--bla2", ...], [[], 0, [all, None]]
    Currently:
        ["--bla1", "--bla2", ...], ["description1", "description2", ...]
    """
    out = execute_command("--help-hidden")
    splits = [a.split(" ", 1) for a in out]
    flags, description = [], []
    for split in splits:
        # first easy case, empty string
        if len(split[0]) == 0:
            continue

        # if we find a colon at the end, its probably a header
        if split[0][-1] == ":":
            continue

        # second easy check, both parts, the flag and the description are valid
        if len(split) == 2:
            flags.append(split[0])
            description.append(split[1])
            continue

        # hard part, if we find a `-` at the beginning of the only stirng its
        # probably a flag. else a cescription
        if split[0][0] == "-":
            flags.append(split)
        else:
            description.append(split)

    return flags, description


def get_opt_flags():
    """
    returns the list of all `opt` flags
    """
    out = execute_command("--help-hidden", OPT_BIN)
    splits = [a.split("- ", 1) for a in out]
    flags, description = [], []
    for split in splits:
        # first easy case, empty string
        if len(split[0]) == 0:
            continue

        # if we find a colon at the end, its probably a header
        if split[0][-1] == ":":
            continue

        # second easy check, both parts, the flag and the description are valid
        if len(split) == 2:
            flags.append(split[0].strip())
            description.append(split[1])
            continue

    return flags, description


def get_opt_optimisations_passes():
    """
    returns all optimisations passed the current opt binary has to offer.
    """
    lines = execute_command("--help-hidden", OPT_BIN)

    found = False
    for i, line in enumerate(lines):
        if "Optimizations available" in line:
            found = True

        if found:
            split = ""
# print(get_clang_flags())
print(get_opt_flags())
