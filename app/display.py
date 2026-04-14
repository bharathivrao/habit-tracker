def print_error(message):
    print(f"Something went wrong: {message}")

def print_success(message):
    print(f"Success: {message}")

def print_habits(habits):
    if not habits:
        print("No habits found.")
        return
    print("Your Habits:")
    for habit in habits:
        print(f"- (Id: {habit[0]}) (Habit Name: {habit[1]}) (Created on: {habit[2]})")

def print_logs(logs):
    if not logs:
        print("No habit logs found.")
        return
    print("Habit Logs:")
    for log in logs:
        status = "Done" if log[2] == 1 else "Not Done"
        print(f"- (Habit: {log[0]}) (Date: {log[1]}) (Status: {status})")

def print_summary(name, current_streak, longest_streak, consistency_rate):
    print(f"Habit: {name}")
    print(f"Current Streak: {current_streak} days")
    print(f"Longest Streak: {longest_streak} days")
    print(f"Consistency Rate: {consistency_rate:.2f}%")
