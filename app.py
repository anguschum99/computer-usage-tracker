# app.py
import time
from datetime import datetime
from tracker.activity_monitor import get_active_window
from tracker.db import init_db, log_activity

def main():
    """Main tracking loop."""
    init_db()

    last_app = None
    last_window = None
    start_time = datetime.now()

    print("🔍 Tracking started... (Press Ctrl + C to stop)")

    try:
        while True:
            app_name, window_title = get_active_window()

            # If the user switched to a different app or window
            if app_name != last_app or window_title != last_window:
                if last_app:
                    end_time = datetime.now()
                    log_activity(last_app, last_window, start_time, end_time)
                    duration = (end_time - start_time).seconds
                    print(f"💾 Logged: {last_app} ({duration}s)")

                start_time = datetime.now()
                last_app = app_name
                last_window = window_title

            time.sleep(2)  # Check every 2 seconds

    except KeyboardInterrupt:
        print("\n🛑 Tracking stopped. Goodbye!")

if __name__ == "__main__":
    main()
