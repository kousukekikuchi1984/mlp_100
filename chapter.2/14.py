import argparse

def head(number=None):
    ary = []
    cur = 1
    with open("hightemp.txt") as f:
        for l in f:
            ary.append(l)
            if number == cur:
                break
            cur += 1
    return "".join(ary)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='head')
    parser.add_argument("-N", "--number")
    args = parser.parse_args()
    number = int(args.number)
    print( head(number) )

