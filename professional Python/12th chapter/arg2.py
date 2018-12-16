import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser(prefix_chars="-")
    # parse.add_argument('/q', "//quiet", action='store_true', dest='quiet', help='suppress output.')
    parse.add_argument('-H', '--host', dest='host', default='localhost', help='the host to connect to. defaults to localhost',
                       type=str)
    args = parse.parse_args()
    print(args.host)
