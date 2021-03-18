from top_k import setting

from top_k.rewriters.rewriters import *

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s] %(message)s',
                    datefmt="%H:%M:%S",
                    handlers=[logging.FileHandler("top_k.log", mode='w'),
                              logging.StreamHandler()])
log = logging.getLogger(__name__)


class WordCounter(object):

    def __init__(self, rewriters: [Rewriter] = []):
        self.rewriters = rewriters

    def process(self, line):
        pass

    def as_dict(self):
        return {}


def process_line(line):
    # word_counter = WordCounter([ignorer, stop_words, lemmatizer])
    #
    # word_counter.process(line)
    # word_counter.as_dict()
    pass


def main():
    log.info('info')
    log.debug('Hello there')
    log.info('infitessimally')
    log.warning('warning')
    log.error('error')

    ignorer = LineIgnorer().settings
    stop_words = StopWordsRemover()
    lemmatizer = Lemmatizer()


    text_file = '../texts/alice.txt'
    # text_file = 'top_k.log'

    with open(text_file) as fp:
        for line in fp:
            process_line(line)


if __name__ == '__main__':
    main()
