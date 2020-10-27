import argparse
import sys
from fileparser import factory


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        type=argparse.FileType()
    )
    parser.add_argument(
        'key',
        type=str
    )
    parser.add_argument(
        '-t', '--filetype',
        type=str.lower,
        choices=factory.get_types() + ['auto'],
        default='auto'
    )

    return parser


def auto_type(filename: str) -> str:
    filetype = filename.split('.')[-1]
    if filetype not in factory.get_types():
        print("Unsupported type")
    return filetype


def parse() -> argparse.Namespace:
    namespace = arg_parser().parse_args(sys.argv[1:])
    if namespace.filetype == 'auto':
        namespace.filetype = auto_type(namespace.file.name)

    return namespace
