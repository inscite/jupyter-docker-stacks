import sys
import subprocess

"""Copyright (c) 2020 Seungkyun Hong. <nah@kakao.com>
   Distributed under the terms of the 3-Clause BSD License.
"""

def main():

    if len(sys.argv) > 1:
        try:
            subproc = subprocess.run(sys.argv[1:], capture_output=True, check=True)
            print(subproc.stdout.decode('UTF-8'), file=sys.stdout)
            print(subproc.stderr.decode('UTF-8'), file=sys.stderr)
        except (subprocess.SubprocessError, subprocess.CalledProcessError) as e:
            print("[E] error occurred while running: {:}".format(str(sys.argv[1:])))
    else:
        pass

    sys.exit(0)
    return

if __name__ == "__main__":
    main()
