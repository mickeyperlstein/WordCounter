from abc import abstractmethod, ABC
from typing import Iterable, List

import attr

import setting
from utils.data_persisters import DataPersister, CsvPersister
from utils.sqlite_persister import SqlLitePersister
import logging

log = logging.getLogger(__name__)


@attr.s
class DataWriter(ABC):
    persisters = list()  # type: List[DataPersister]

    def validate_persisters(self) -> bool:
        if setting.SQLITE_OUTPUT_ACTIVE:
            persister = SqlLitePersister()
            ok = persister.validate_target()
            if ok:
                self.persisters.append(persister)
            else:
                log.error(f'Failed to validate Persister {persister}')

        if setting.CSV_OUTPUT_ACTIVE:
            csv_persister = CsvPersister()
            ok = csv_persister.validate_target()
            if ok:
                self.persisters.append(csv_persister)
            else:
                log.error(f'Failed to validate Persister {csv_persister}')

        return len(self.persisters) > 0

    def write(self, dic1: dict, project_name):
        for p in self.persisters:
            p.persist(dic1)
