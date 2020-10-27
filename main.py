import consarg
import fileparser
import loggerinit


def main():
    logger = loggerinit.get_logger()
    logger.info("Program started")
    try:
        namespace = consarg.parse()
        logger.debug(namespace)

        parser = fileparser.get_parser(namespace.extension)
        logger.debug("The parser was received successfully")
        logger.debug(parser)

        res = parser.find(namespace.file, namespace.key)
        logger.info("The value was found successfully")
        logger.info(res)
    except KeyError as e:
        logger.error("Key not found")
        logger.error(f"Key: {e}")
        print("Error: Key not found")
    except FileNotFoundError as e:
        logger.error("File not found")
        logger.error(e)
        print("Error: File not found")
    except AttributeError as e:
        logger.error("Error: File extension parsing error")
        logger.error(e)
    else:
        print(res)
    finally:
        logger.info("The program is finished\n")


if __name__ == '__main__':
    main()
