import argparse

def upload(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

if __name__ == "__main__":
    # upload(arg1, arg2, arg3)

    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol')
    parser.add_argument('--url')
    parser.add_argument('--tld')
    args = parser.parse_args()
    
    print(args.protocol, args.url, args.tld)