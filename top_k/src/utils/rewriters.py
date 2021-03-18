import abc
import logging
import os
from typing import List

import attr
import nltk
from dotdict import dotdict
from nltk import word_tokenize
from nltk.corpus import stopwords

from utils.helpers import eval_bool

log = logging.getLogger(__name__)


def log_in_and_out(function):
    def wrapper(line_in):
        log.debug(f'I: {line_in}')
        ret = function()
        log.debug(f'O: {ret}')
        return ret


@attr.s
class Rewriter(abc.ABC):
    settings = attr.ib(default=None)
    has_loaded = attr.ib(default=False)
    rewritten_words = list()
    active = False

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

    @abc.abstractmethod
    def rewrite_word_array(self, word_tokens: List[str]) -> List[str]:
        pass

    def load_settings(self):
        self.settings = dotdict({'type': self.name,
                                 'active': eval_bool(os.getenv(f'{self.name}_ACTIVE', default='NO')),
                                 'path_location': os.getenv(f'{self.name}_path_LOCATION', default=None)
                                 })
        self.has_loaded = self._init_db()
        self.active = self.settings.active


@attr.s
class StopWordsRemover(Rewriter):
    MORE_STOPS = {'\n', '\t', "'", "`", '"', '.', '*', ',', '!', ';', '(', ')', '[', ']', 'A', '?', ':',
                  '“', '”', '’', 'I'}

    def _init_db(self) -> str:
        nltk.download('stopwords')
        self.words = set(stopwords.words('english')).union(self.MORE_STOPS)
        return True

    @property
    def name(self):
        return 'STOP_WORDS'

    def rewrite_line(self, line) -> str:
        word_tokens = word_tokenize(line)
        self.rewrite_word_array(word_tokens)

        return ' '.join(word_tokens)

    def rewrite_word_array(self, word_tokens: List[str]) -> List[str]:
        filtered_sentence = [w for w in word_tokens if w not in self.words]
        self.rewritten_words = list(filtered_sentence)

        return self.rewritten_words


@attr.s
class LineIgnorer(StopWordsRemover):

    @property
    def name(self):
        return 'LINE_IGNORE'


@attr.s
class Lemmatizer(Rewriter):

    def _init_db(self) -> str:
        from nltk.stem import WordNetLemmatizer
        nltk.download('wordnet')
        self.lemmatizer = WordNetLemmatizer()

        return True

    @property
    def name(self):
        return 'LEMMATIZER'

    def rewrite_line(self, line) -> str:
        word_tokens = word_tokenize(line)
        self.rewrite_word_array(word_tokens)
        return ' '.join(self.rewritten_words)

    def rewrite_word_array(self, word_tokens: List[str]) -> List[str]:
        lemmatized_arr = [self.lemmatizer.lemmatize(w) for w in word_tokens]
        self.rewritten_words = list(lemmatized_arr)
        return self.rewritten_words
