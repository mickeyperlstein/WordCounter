import os

from dotenv import load_dotenv as _load_

from utils.helpers import eval_bool

_load_(verbose=True)
top_k = int(os.getenv('TOP_K'))

SQLITE_OUTPUT_FILE = os.getenv('SQLITE_OUTPUT_FILE')
SQLITE_OUTPUT_ACTIVE = eval_bool(os.getenv('SQLITE_OUTPUT_ACTIVE'))

CSV_OUTPUT_FILE = os.getenv('CSV_OUTPUT_FILE')
CSV_OUTPUT_ACTIVE = eval_bool(os.getenv('CSV_OUTPUT_ACTIVE'))
