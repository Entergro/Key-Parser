import consarg
import fileparser


def main():
    namespace = consarg.parse()
    parser = fileparser.get_parser(namespace.filetype)
    print(parser.find(namespace.file, namespace.key))


if __name__ == '__main__':
    main()
