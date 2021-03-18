import logging
from collections import Counter
from typing import Union, List

from .rewriters import Rewriter

log = logging.getLogger('')


class WordCounter:

    def __init__(self, rewriters: [Rewriter] = []):
        self.rewriters = list(filter(lambda f: bool(f.active) is True, rewriters))  # type: List[Rewriter]

    def process(self, line) -> Counter:

        if len(line) > 1:
            log.debug(f'I: {line}')
            first_rewriter = self.rewriters[0]
            first_rewriter.rewrite_line(line)
            tokens = first_rewriter.rewritten_words

            for r in self.rewriters[1:]:
                tokens = r.rewrite_word_array(tokens)  # add line and tokens usage

            c = Counter(tokens)
            return c
