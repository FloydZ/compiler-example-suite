#!/usr/bin/env python3
"""
wrapper around objdump
"""

from subprocess import Popen, PIPE, STDOUT
from typing import Tuple, List

# path to the `objdump` executable 
objdump = "objdump"
# flags passed to `objdump`
objdump_flags = ["--inline", "-l", "--disassembler-options=intel64"]
# symbols to dump
symbols = [
    "die",
    "ecalloc"
]
# path to the binary/library/object file to analyze.
path = "dwm/dwm" 
# patterns of instructions to search within the disassembly.
patterns = [
    "div",
    "idiv",
    "lea",
]


def run_objdump(path: str,
                symbol: str) -> Tuple[bool, List[str]]:
    """
    :param path: path to the object/library file to dump
    :param symbol: symbol to disassembler
    :return (
        true/false: if the process succeded,
        list[str]: output of `objdump` as a list of string which contain each 
                line of the output of `objdump`.
    )
    """
    cmd = [objdump] + objdump_flags + [ f"--disassemble={symbol}", path]
    print(cmd)

    with Popen(cmd, stdout=PIPE, stderr=STDOUT, universal_newlines=True) as p:
        p.wait()
        
        assert p.stdout
        data = p.stdout.readlines()
        data = [str(a).replace("b'", "")
                .replace("\\n'", "")
                .replace("\\t'", "")
                .lstrip() for a in data]
        print(p.returncode)
        print(data)
        return p.returncode == 0, data


def parse_objdump(lines: List[str],
                  patterns: List[str]) -> Tuple[bool, List[int]]:
    """
    :param lines:
    :param patterns:
    """
    ret = []
    for i, line in enumerate(lines):
        for pattern in patterns:
            if pattern in line:
                ret.append(i)
    return len(ret) > 0, ret


b, lines = run_objdump(path, symbols[0])
assert b
b, solutions = parse_objdump(lines, patterns)
# assert b
print(solutions)
