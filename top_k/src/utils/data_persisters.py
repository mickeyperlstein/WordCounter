import abc
import logging
from typing import List

import attr

import setting

log = logging.getLogger(__name__)


@attr.s
class DataPersister(abc.ABC):
    persisters = list()  # type: List[DataPersister]

    @abc.abstractmethod
    def validate_target(self) -> bool:
        pass

    @abc.abstractmethod
    def persist(self, dict1: dict, project_name: str):
        pass


@attr.s
class CsvPersister(DataPersister):

    def validate_target(self) -> bool:
        return True

    def persist(self, dict1: dict, project_name):
        header = 'word, count\n'
        lines = [header].extend([f'{k}, {v}\n' for k, v in dict1.items()])

        filename_with_path = setting.CSV_OUTPUT_FILE
        filename = f'{project_name}_{filename_with_path}'

        with open(filename, 'wt') as fp:
            fp.writelines(lines)
