from datetime import date
from app.db import get_db_connection

def add_habit(name):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO habits (name, created_at) VALUES (?, ?)", (name, date.today().isoformat()))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding habit: {e}")
        return False
    finally:
        if conn:
            conn.close()
            
def list_habits():
    # Code to retrieve and display all habits from the database
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM habits")
        habits = cursor.fetchall()
        return habits
    except Exception as e:
        print(f"Error viewing habits: {e}")
        return []
    finally:
        if conn:
            conn.close() 

def get_habit_logs(name):
    # Code to retrieve and display habit logs from the database
    conn = None
    try:        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT hl.date
            FROM habit_logs hl
            JOIN habits h ON hl.habit_id = h.id
            WHERE h.name = ?
            ORDER BY hl.date ASC
        """, (name,))
        logs = cursor.fetchall()
        return logs
    except Exception as e:
        print(f"Error viewing habit logs: {e}")
        return []
    finally:        
        if conn:
            conn.close()  

def mark_done(habit_name, log_date=None):
    # Code to mark a habit as done for the current day
    conn = None
    try:        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM habits WHERE name = ?", (habit_name,))
        habit = cursor.fetchone()
        if not habit:
            print(f"Habit '{habit_name}' not found.")
            return False
        habit_id = habit[0]
        date_str = date.today().isoformat()
        if log_date:
            date_str = log_date.isoformat()
        cursor.execute("INSERT OR REPLACE INTO habit_logs (habit_id, date, status) VALUES (?, ?, ?)", (habit_id, date_str, 1))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error marking habit as done: {e}")
        return False
    finally:        
        if conn:
            conn.close()    
    

