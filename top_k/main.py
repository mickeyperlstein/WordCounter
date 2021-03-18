from top_k import setting
from top_k.utils.WordCounter import WordCounter
from top_k.utils.rewriters import *

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s] %(message)s',
                    datefmt="%H:%M:%S",
                    handlers=[logging.FileHandler("top_k.log", mode='w'),
                              logging.StreamHandler()])
log = logging.getLogger(__name__)


def process_line(line, ignorers) -> dict:
    word_counter = WordCounter(ignorers)
    word_counter.process(line)
    words = word_counter.as_dict()
    return words


def main():
    log.info('info')
    log.debug('Hello there')
    log.info('infitessimally')
    log.warning('warning')
    log.error('error')

    line_ignorer = LineIgnorer()
    stop_words = StopWordsRemover()
    lemmatizer = Lemmatizer()

    ignorers = [line_ignorer, stop_words, lemmatizer]
    for r in ignorers:  # type [Rewriter]
        r.load_settings()

    text_file = '../texts/alice.txt'
    # text_file = 'top_k.log'

    with open(text_file) as fp:
        for line in fp:
            process_line(line, ignorers=ignorers)


if __name__ == '__main__':
    main()
