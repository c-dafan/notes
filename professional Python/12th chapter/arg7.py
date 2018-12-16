import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-c', '--config-file',
                       default='./text.txt',
                       dest='config',
                       help='the configuration file to use',
                       type=argparse.FileType('r'))
    args = parse.parse_args()
    print(args.config.read())
