import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('--cheese', choices=('provolone', 'swiss', 'cheddar', 'american'),
                       default='swiss', dest='cheese', help='the kind of cheese to use', )
    args = parse.parse_args()
    print(args.cheese)
