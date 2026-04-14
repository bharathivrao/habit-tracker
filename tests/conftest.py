import os
from pathlib import Path

import pytest

from app.db import init_db

TEST_DB_PATH = Path("tests/data/habits_test.db")
os.environ["HABIT_TRACKER_DB"] = str(TEST_DB_PATH)

@pytest.fixture(autouse=True)
def reset_database():
    TEST_DB_PATH.unlink(missing_ok=True)
    init_db()
    yield
