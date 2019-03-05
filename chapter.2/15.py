
import argparse

def tail(number=None):
    ary = []
    with open("hightemp.txt") as f:
        for l in f:
            ary.append(l)
    return "".join(ary[-number:])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='head')
    parser.add_argument("-N", "--number")
    args = parser.parse_args()
    number = int(args.number)
    print( tail(number) )
