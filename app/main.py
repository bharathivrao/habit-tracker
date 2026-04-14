import datetime
from app.analytics import calculate_consistency
from app.db import init_db
from app.cli import parse_args
from app.display import print_error, print_logs, print_success, print_habits, print_summary
from app.habits import add_habit, list_habits, get_habit_logs, mark_done
from app.streaks import calculate_current_streak, calculate_longest_streak

def main():
    init_db()
    print("Welcome to the Habit Tracker!")
    # Additional code for the main application logic can be added here
    args = parse_args()

    if args is None:
        print_error("No arguments provided.")
        return

    if args.command == "add-habit":
        name = args.name.strip()
        if not name:
            print_error("Habit name cannot be empty.")
            return
        success = add_habit(args.name)
        if success:
            print_success("Habit added successfully.")
        else:
            print_error("Failed to add habit.")
        print_habits(list_habits())

    elif args.command == "mark-done":
        habit_name = args.name.strip()
        date_str = args.date.strip() if args.date else None
        if not habit_name:
            print_error("Habit name cannot be empty.")
            return
        success = mark_done(habit_name, date_str)
        if success:
            print_success(f"Habit '{habit_name}' marked as done.")
        else:
            print_error(f"Failed to mark habit '{habit_name}' as done.")

    elif args.command == "view-logs":
        habit_name = args.name.strip() if args.name else None
        if habit_name:
            logs = get_habit_logs(habit_name)
            print_logs(logs)
        else:
            print_error("Habit name is required to view logs.")

    elif args.command == "show-summary":
        habit_name = args.name.strip() if args.name else None
        if not habit_name:
            print_error("Habit name is required to show summary.")
            return

        log_dates = get_habit_logs(habit_name)
        current = calculate_current_streak(log_dates)
        longest = calculate_longest_streak(log_dates)
        consistency = calculate_consistency(log_dates, start_date=datetime.date(2026, 4, 10), end_date=datetime.date(2026, 4, 13))

        print_summary(habit_name, current, longest, consistency)

    else:
        print_error("Unknown command.")


