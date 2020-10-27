from abc import abstractmethod
from typing import List


class FileParser:
    @abstractmethod
    def find(self, file, key: str):
        if key == '*':
            return self._parse_aggregate(file)
        else:
            return self._parse_at_key(file, self.parse_key(key))

    @abstractmethod
    def _parse_at_key(self, file, key: List[str]):
        pass

    @abstractmethod
    def _parse_aggregate(self, file):
        pass

    @staticmethod
    def parse_key(key: str):
        return key.split('.')
