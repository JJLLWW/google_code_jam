import subprocess as subp
import sys

def main():
    if len(sys.argv) < 3:
        print(f"Usage: test.py [script] [data]")
        return 0
    print(f"running {sys.argv[1]} with data {sys.argv[2]}")
    # p = subp.Popen(["py", sys.argv[1]], stdout=subp.PIPE, stdin=subp.PIPE, stderr=subp.PIPE)
    with open(sys.argv[2]) as data:
        content = data.read()
        # output = p.communicate(input=content)[0]
        completed = subp.run(["py", sys.argv[2]], input=content, capture_output=True)
        print(completed.stdout)

main()