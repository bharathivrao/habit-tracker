import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_habit_parser = subparsers.add_parser("add-habit")
    add_habit_parser.add_argument("--name", required=True, help="Habit name")

    mark_done_parser = subparsers.add_parser("mark-done")
    mark_done_parser.add_argument("--name", required=True, help="Name of the habit to mark as done")
    mark_done_parser.add_argument("--date", help="Date for which to mark the habit as done")

    view_logs_parser = subparsers.add_parser("view-logs")
    view_logs_parser.add_argument("--name", help="Name of the habit for which to view logs")
    
    show_summary_parser = subparsers.add_parser("show-summary")
    show_summary_parser.add_argument("--name", help="Name of the habit for which to show summary")

    return parser.parse_args()