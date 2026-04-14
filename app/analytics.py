def calculate_consistency(log_dates, start_date=None, end_date=None):
    completed_days = len(log_dates)
    total_days_in_range = (end_date - start_date).days + 1 if start_date and end_date else 1
    consistency_percent = (completed_days / total_days_in_range) * 100 if total_days_in_range > 0 else 0
    return consistency_percent