

import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument("-br", "--branch", help="StaticAnalysis branch name", required=True)
branch_name = parser.parse_args().branch

with fileinput.input("./.github/workflows/test.yml", inplace=True) as file:
    for line in file:
        if line.strip().startswith("uses: JacobDomagala/StaticAnalysis@"):
            print(f"      uses: JacobDomagala/StaticAnalysis@{branch_name}")
        else:
            print(f"{line}", end='')

