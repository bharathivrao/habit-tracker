
from app.streaks import calculate_current_streak, calculate_longest_streak
import datetime

def test_empty_logs():
    # Test case 1: No log dates
    log_dates = []
    assert calculate_current_streak(log_dates) == 0
    assert calculate_longest_streak(log_dates) == 0

def test_single_day_streak():
    # Test case 2: Single log date (today)
    today = datetime.date.today()
    log_dates = [today]
    assert calculate_current_streak(log_dates) == 1
    assert calculate_longest_streak(log_dates) == 1

def test_consecutive_days_streak():
    # Test case 3: Consecutive log dates (3 days)
    today = datetime.date.today()
    log_dates = [today - datetime.timedelta(days=2), today - datetime.timedelta(days=1), today]
    assert calculate_current_streak(log_dates) == 3
    assert calculate_longest_streak(log_dates) == 3

def test_non_consecutive_days():
    # Test case 4: Non-consecutive log dates
    today = datetime.date.today()
    log_dates = [today - datetime.timedelta(days=5), today - datetime.timedelta(days=3), today - datetime.timedelta(days=1)]
    assert calculate_current_streak(log_dates) == 0
    assert calculate_longest_streak(log_dates) == 1

def test_multiple_streaks():
    # Test case 5: Multiple streaks
    today = datetime.date.today()
    log_dates = [today - datetime.timedelta(days=10), today - datetime.timedelta(days=9), today - datetime.timedelta(days=7), today - datetime.timedelta(days=6), today - datetime.timedelta(days=5)]
    assert calculate_current_streak(log_dates) == 0
    assert calculate_longest_streak(log_dates) == 3

    
    

    

    

    