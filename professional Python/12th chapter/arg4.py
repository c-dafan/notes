import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('--madlib',
                       default=['fox', 'dogs'],
                       dest='madlib',
                       help='two words to place in the madlib',
                       nargs=2)
    args = parse.parse_args()
    print(args.madlib)
