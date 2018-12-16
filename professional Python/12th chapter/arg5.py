import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('--addends',
                       dest='addends',
                       help='integers to provide a sum of ',
                       nargs='+',
                       required=True,
                       type=int)
    args = parse.parse_args()
    print(args.addends)
