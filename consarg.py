import argparse
import sys
from fileparser import factory


def arg_parser():
    parser = argparse.ArgumentParser(exit_on_error=False)
    parser.add_argument(
        'file',
        type=argparse.FileType()
    )
    parser.add_argument(
        'key',
        type=str
    )
    parser.add_argument(
        '-e', '--extension',
        type=str.lower,
        choices=factory.get_ext() + ['auto'],
        default='auto'
    )

    return parser


def auto_ext(filename: str) -> str:
    file_ext = filename.split('.')[-1]
    if file_ext not in factory.get_ext():
        raise RuntimeError(f"Unsupported extension: {file_ext}")
    return file_ext


def parse():
    try:
        namespace = arg_parser().parse_args(sys.argv[1:])
        if namespace.extension == 'auto':
            namespace.extension = auto_ext(namespace.file.name)
        return namespace
    except argparse.ArgumentError as e:
        if e.argument_name == 'file':
            raise FileNotFoundError(e)
        if e.argument_name == '-e/--extension':
            raise AttributeError(e)
    except RuntimeError as e:
        raise RuntimeError(e)
