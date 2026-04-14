import datetime
from app.habits import add_habit, list_habits, mark_done, get_habit_logs


def extract_logged_dates(logs):
    normalized_dates = []

    for log in logs:
        if isinstance(log, datetime.date):
            normalized_dates.append(log)
        elif isinstance(log, str):
            normalized_dates.append(datetime.date.fromisoformat(log))
        elif isinstance(log, tuple):
            if len(log) >= 2:
                normalized_dates.append(datetime.date.fromisoformat(log[1]))
            elif len(log) == 1:
                normalized_dates.append(datetime.date.fromisoformat(log[0]))

    return normalized_dates


def test_add_habit():
    habit_name = "Exercise_add_habit"
    add_habit(habit_name)

    habits = list_habits()
    habit_names = [habit[1] if isinstance(habit, tuple) else habit for habit in habits]

    assert habit_name in habit_names


def test_mark_done():
    habit_name = "Exercise_mark_done"
    add_habit(habit_name)
    today = datetime.date(2026, 4, 13)
    mark_done(habit_name, today)
    logs = get_habit_logs(habit_name)
    logged_dates = extract_logged_dates(logs)
    assert logged_dates == [today]


def test_mark_done_multiple_days():
    habit_name = "Exercise_multiple_days"
    add_habit(habit_name)
    day1 = datetime.date(2026, 4, 13)
    day2 = datetime.date(2026, 4, 14)
    mark_done(habit_name, day1)
    mark_done(habit_name, day2)
    logs = get_habit_logs(habit_name)
    logged_dates = extract_logged_dates(logs)
    assert logged_dates == [day1, day2]


def test_mark_done_non_consecutive_days():
    habit_name = "Exercise_non_consecutive_days"
    add_habit(habit_name)
    day1 = datetime.date(2026, 4, 13)
    day2 = datetime.date(2026, 4, 15)
    mark_done(habit_name, day1)
    mark_done(habit_name, day2)
    logs = get_habit_logs(habit_name)
    logged_dates = extract_logged_dates(logs)
    assert logged_dates == [day1, day2]


def test_mark_done_duplicate_days():
    habit_name = "Exercise_duplicate_days"
    add_habit(habit_name)
    day = datetime.date(2026, 4, 13)
    mark_done(habit_name, day)
    mark_done(habit_name, day)
    logs = get_habit_logs(habit_name)
    logged_dates = extract_logged_dates(logs)
    assert logged_dates == [day]
