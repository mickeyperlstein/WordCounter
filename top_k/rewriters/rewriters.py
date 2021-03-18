import abc
import logging
import os

import attr
from dotdict import dotdict

log = logging.getLogger(__name__)


@attr.s
class Rewriter(abc.ABC):
    settings = attr.ib(init=False)

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def remove(self, line) -> str:
        pass

    def load_settings_from(self):
        self.settings = dotdict({'type': self.name,
                                 'ignorer_active': os.getenv(f'{self.name}_ACTIVE', default='NO'),
                                 'ignorer_csv_location': os.getenv(f'{self.name}_CSV_LOCATION', default=None)
                                 })


class LineIgnorer(Rewriter):

    @property
    def name(self):
        return 'LINE_IGNORE'

    def remove(self, line) -> str:
        return line


class StopWordsRemover(Rewriter):

    @property
    def name(self):
        return 'STOP_WORDS'

    def remove(self, line) -> str:
        return line


class Lemmatizer(Rewriter):

    @property
    def name(self):
        return 'LEMMATIZER'

    def remove(self, line) -> str:
        return line
