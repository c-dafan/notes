import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('addends',
                       help='Integers to provide a sum of',
                       nargs="+",
                       type=int)
    args = parse.parse_args()
    print(args.addends)
