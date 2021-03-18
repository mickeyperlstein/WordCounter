import statistics
from collections import Counter

from top_k.src import setting
from top_k.src.utils.WordCounter import WordCounter
from top_k.src.utils.rewriters import *
from utils.data_writers import DataWriter

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s] %(message)s',
                    datefmt="%H:%M:%S",
                    handlers=[logging.FileHandler("../top_k.log", mode='w'), logging.StreamHandler()])
log = logging.getLogger(__name__)


def process_line(line, ignorers) -> Counter:
    if len(line) > 1:
        word_counter = WordCounter(ignorers)
        words = word_counter.process(line)

    return words


def main():
    # log.info('info')
    # log.debug('Hello there')
    # log.info('infitessimally')
    # log.warning('warning')
    # log.error('error')

    line_ignorer = LineIgnorer()
    stop_words = StopWordsRemover()
    lemmatizer = Lemmatizer()

    ignorers = [line_ignorer, stop_words, lemmatizer]
    for r in ignorers:  # type [Rewriter]
        r.load_settings()

    data_persister = DataWriter()
    data_persister.validate_persisters()

    inputs = list()

    text_file = '../texts/alice.txt'
    project_name = 'Alice in wonderland'

    inputs.append((project_name, text_file))

    run_on_file(data_persister, ignorers, project_name, text_file)


def run_on_file(data_persister, ignorers, project_name, text_file):
    all_doc = Counter()
    counters = list()
    with open(text_file) as fp:
        for line in fp:
            if len(line) > 1:

                if line[-1] == '\n':
                    line = line[:-1]

                ctr = process_line(line.lower(), ignorers=ignorers)
                counters.append(ctr)
    log.info(f'Reducing {len(counters)} counters ...')
    for d in counters:
        all_doc.update(d)
    log.info(f'Calculating top_k for {project_name}')
    top_k = all_doc.most_common(n=setting.top_k)
    vals = sorted(all_doc.values())
    median = statistics.median(vals)
    mean = statistics.mean(vals)
    log.info(f'{project_name} => MEDIAN: {median}   MEAN: {mean}')
    log.info(f'{project_name} => top_k k={setting.top_k} {top_k}')
    log.info('persisting')
    data_persister.write(top_k, project_name)


if __name__ == '__main__':
    main()
