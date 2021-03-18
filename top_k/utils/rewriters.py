import abc
import logging
import os

import attr
import nltk
from dotdict import dotdict
from nltk import word_tokenize
from nltk.corpus import stopwords

log = logging.getLogger(__name__)


@attr.s
class Rewriter(abc.ABC):

    settings = attr.ib(default=None)
    has_loaded = attr.ib(default=False)

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def _init_db(self) -> bool:
        return True

    @abc.abstractmethod
    def rewrite_line(self, line) -> str:
        pass

    def load_settings(self):
        self.settings = dotdict({'type': self.name,
                                 'active': os.getenv(f'{self.name}_ACTIVE', default='NO'),
                                 'path_location': os.getenv(f'{self.name}_path_LOCATION', default=None)
                                 })
        self.has_loaded = self._init_db()

@attr.s
class StopWordsRemover(Rewriter):

    def _init_db(self) -> str:

        nltk.download('stopwords')
        nltk.download('punkt')
        self.words = set(stopwords.words('english'))
        return True

    @property
    def name(self):
        return 'STOP_WORDS'

    def rewrite_line(self, line) -> str:

        word_tokens = word_tokenize(line)
        filtered_sentence = [w for w in word_tokens if w not in self.words]

        return ' '.join(filtered_sentence)

@attr.s
class LineIgnorer(StopWordsRemover):

    @property
    def name(self):
        return 'LINE_IGNORE'


@attr.s
class Lemmatizer(Rewriter):

    def _init_db(self) -> str:
        return True


    @property
    def name(self):
        return 'LEMMATIZER'

    def rewrite_line(self, line) -> str:
        return line
