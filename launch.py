import sys

def upload(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

if __name__ == "__main__":
    _, arg1, arg2, arg3 = sys.argv
    upload(arg1, arg2, arg3)