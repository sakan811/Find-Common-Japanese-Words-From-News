import sqlite3

import pytest

from jp_news_scraper_pipeline.pipeline import load_to_sqlite
from main import start_news_scraper_pipeline


def test_main_process():
    sqlite_db = 'japan_news_test.db'
    df = start_news_scraper_pipeline(sqlite_db)
    load_to_sqlite(df, sqlite_db)

    with sqlite3.connect(sqlite_db) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM JapanNews')
        rows = c.fetchall()
        assert len(rows) > 0

    with sqlite3.connect(sqlite_db) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM NewsUrls')
        rows = c.fetchall()
        assert len(rows) > 0


if __name__ == '__main__':
    pytest.main([__file__])
