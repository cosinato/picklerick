#!/usr/bin/env python3
#
import argparse

__version__ = '0.1.0'

def parse_args(argv=None):
    parsed = argparse.ArgumentParser(description='Picklerick LLC, Command Line Utility')
    parsed.add_argument('hello', help='Greetings and Salutations')
    parsed.add_argument(
        '-n',
        '--name',
        dest='name',
        type=str,
        default='World',
        help='')
    return parsed.parse_args(argv)


def main():
    args = parse_args()
    name = args.name
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()
