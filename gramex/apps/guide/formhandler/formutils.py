import os.path
import gramex.cache
from gramex.config import app_log, str_utf8
from sqlalchemy import create_engine


folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, 'database.sqlite3')
engine = create_engine('sqlite:///%s' % filepath, encoding=str_utf8)
examplespath = os.path.normpath(os.path.join(folder, 'examples.yaml'))
examples = gramex.cache.open(examplespath, 'yaml')


def flagsdb():
    """
    fetch flags data into database.sqlite3/flags
    """
    if os.path.exists(filepath):
        os.unlink(filepath)
    url = os.path.join(folder, 'flags.csv')
    flags = gramex.cache.open(url, encoding='cp1252')
    flags.to_sql('flags', engine, index=False)
    app_log.info('database.sqlite3 created with flags table')
