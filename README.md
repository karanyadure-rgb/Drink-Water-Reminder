💧 Drink Water Reminder

A tiny Python script that sends a desktop notification every hour reminding you to drink water. Set it, forget it, stay hydrated.

Why I made this

I kept forgetting to drink water while coding for hours. Didn't want a browser extension or a heavy app — just a simple script I can run in the background and ignore until it pings me.

Requirements


Python 3.x
plyer — for cross-platform desktop notifications
schedule — for running the reminder on a timer


Install dependencies:

bashpip install plyer schedule

Usage

bashpython water_reminder.py

You'll see this in the terminal:

Drink Water Reminder started!!
Press Ctrl+C to exit

Then every hour, a desktop notification will pop up:


Hydration Reminder
You need to drink some water



To stop it, just press Ctrl+C:

Reminder stopped.

How it works


schedule runs send_notification() every hour
plyer sends the actual OS-level desktop notification (works on Windows, macOS, and Linux)
The while True loop checks every 60 seconds if a scheduled job is due
Wrapped in a try/except KeyboardInterrupt so Ctrl+C exits cleanly without a stack trace
