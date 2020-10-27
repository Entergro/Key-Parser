from typing import List
from modules.object_module import FileParser
from abc import ABC
import json


class JsonParser(FileParser, ABC):
    def _parse_at_key(self, file, key: List[str]):
        data = json.load(file)
        for k in key:
            data = data[k if not k.isdigit() else int(k)]
        return json.dumps(data, indent=4)

    def _parse_aggregate(self, file):
        data = json.load(file)
        return json.dumps(data, indent=4)
