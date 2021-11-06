import sys

print(sys.version)
print(f"{sys.version_info} + {sys.api_version}")

for line in sys.stdin:
    if "q" == line.rstrip():
        break
    print(f"input = {line}") 
print("Exit")

sys.stdout.write('hdmtp')

def print_to_stderr(*a):
    print(*a, file=sys.stderr)

print_to_stderr("hdmtp is here")
print("\n")

####################################################
# *args in Python example
def args_in_py(*args):
    for arg in args:
        print(arg)

args_in_py("wow", "that", "is", "really", "cool")
####################################################