"""Command-line interface for pup name generator."""

import argparse

from generator import generate
from utils import generate_with_uuid, unique
from validator import validate


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate or validate pup names.")
    subparsers = parser.add_subparsers(dest="command")

    gen = subparsers.add_parser("generate", help="Generate pup names")
    gen.add_argument("-w", "--words", type=int, default=3, help="Number of words (default: 3)")
    gen.add_argument("-s", "--separator", default="-", help="Word separator (default: '-')")
    gen.add_argument("-n", "--count", type=int, default=1, help="Number of names to generate (default: 1)")
    gen.add_argument("--uuid", action="store_true", help="Append short UUID suffix for uniqueness")

    val = subparsers.add_parser("validate", help="Validate a pup name")
    val.add_argument("name", help="Name to validate")
    val.add_argument("--separator", default="-", help="Word separator (default: '-')")

    args = parser.parse_args()

    if args.command == "generate":
        used = set()
        for _ in range(args.count):
            if args.uuid:
                print(generate_with_uuid(args.words, args.separator, used))
            else:
                print(unique(used, args.words, args.separator))

    elif args.command == "validate":
        print("Valid" if validate(args.name, args.separator) else "Invalid")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
