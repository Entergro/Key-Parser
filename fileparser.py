from modules import json


class _ParserFactory:
    def __init__(self):
        self._creators = {}

    def register_ext(self, format, creator):
        self._creators[format] = creator

    def get_parser(self, extension):
        creator = self._creators.get(extension)
        if not creator:
            raise ValueError(extension)
        return creator()

    def get_ext(self):
        return list(self._creators.keys())


factory = _ParserFactory()
factory.register_ext('json', json.JsonParser)


def get_parser(file_ext: str):
    return factory.get_parser(file_ext)
