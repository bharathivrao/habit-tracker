# habit-tracker

A simple CLI habit tracker that stores habits, logs completion dates, and calculates streaks and consistency.

## Features

- Add new habits
- Mark habits as done for a specific date
- View habit logs
- Show habit summary with current streak, longest streak, and consistency rate

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd habit-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> Note: This project currently uses only Python standard library modules, so `requirements.txt` may be empty.

## Usage

Run the application with:

```bash
python run.py <command> [options]
```

### Commands

- Add a habit:
  ```bash
  python run.py add-habit --name "Exercise"
  ```

- Mark a habit as done:
  ```bash
  python run.py mark-done --name "Exercise"
  ```

- Mark a habit as done for a specific date:
  ```bash
  python run.py mark-done --name "Exercise" --date 2026-04-13
  ```

- View logs for a habit:
  ```bash
  python run.py view-logs --name "Exercise"
  ```

- Show habit summary:
  ```bash
  python run.py show-summary --name "Exercise"
  ```

## Database

- The app stores data in `data/habits.db`
- Tests use a separate database at `tests/data/habits_test.db`

## Testing

Run the test suite with:

```bash
PYTHONPATH=. pytest -q
```

## Project Structure

- `run.py` — entry point for the CLI application
- `app/main.py` — main command dispatcher
- `app/cli.py` — CLI argument parsing
- `app/db.py` — SQLite database connection and schema initialization
- `app/habits.py` — habit management functions
- `app/streaks.py` — streak calculation logic
- `app/analytics.py` — consistency calculation
- `app/display.py` — CLI output formatting
- `tests/` — unit tests
