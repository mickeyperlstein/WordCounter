import logging
from typing import Union, List

from .rewriters import Rewriter

log = logging.getLogger('')


class WordCounter:

    def __init__(self, rewriters: [Rewriter] = []):
        self.rewriters = rewriters

    def process(self, line):
        for r in self.rewriters:
            if r.settings.active:
                log.debug(f'rewriter : {r}')
                log.debug(f'INPUT : {line}')
                line = r.rewrite_line(line)
                log.debug(f'OUTPUT : {line}')

    def as_dict(self):
        return {'abc': 8, 'the': 9}
