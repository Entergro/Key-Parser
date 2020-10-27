from modules import json


class _ParserFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_parser(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()

    def get_types(self):
        return list(self._creators.keys())


factory = _ParserFactory()
factory.register_format('json', json.JsonParser)


def get_parser(file_format: str):
    return factory.get_parser(file_format)
