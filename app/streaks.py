import datetime

def calculate_current_streak(log_dates, today=None):
    try:
        if not log_dates:
            return 0
        if today is None:
            today = datetime.date.today()
        log_dates = sorted(set(log_dates))
        current_streak = 0
        for date in reversed(log_dates):
            if date == today - datetime.timedelta(days=current_streak):
                current_streak += 1
            else:
                break
        return current_streak
    except Exception as e:
        print(f"Error calculating current streak: {e}")
        return 0

def calculate_longest_streak(log_dates):
    try:
        if not log_dates:
            return 0
        log_dates = sorted(set(log_dates))
        longest_streak = 0
        current_streak = 1
        for i in range(1, len(log_dates)):
            if log_dates[i] == log_dates[i-1] + datetime.timedelta(days=1):
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
        longest_streak = max(longest_streak, current_streak)
        return longest_streak
    except Exception as e:
        print(f"Error calculating longest streak: {e}")
        return 0