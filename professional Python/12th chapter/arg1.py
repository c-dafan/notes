import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser(prefix_chars="/")
    parse.add_argument('/q', "//quiet", action='store_true', dest='quiet', help='suppress output.')
    args = parse.parse_args()
    print(args.quiet)
