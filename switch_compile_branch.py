

import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument("-br", "--branch", help="Compile Result branch name", required=True)
branch_name = parser.parse_args().branch

with fileinput.input("./.github/workflows/test.yml", inplace=True) as file:
    for line in file:
        if line.strip().startswith("uses: JacobDomagala/CompileStatus@"):
            print(f"      uses: JacobDomagala/CompileStatus@{branch_name}")
        else:
            print(f"{line}", end='')

