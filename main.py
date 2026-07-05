import time
from plyer import notification
import schedule


def send_notification():
    try:
        notification.notify(
            title="Hydration Reminder",
            message="You need to drink some water",
            app_name="Water Reminder",
            timeout=10)
    except Exception as e:
        print("Notification Error!!",e) 

schedule.every(1).hour.do(send_notification)

print("Drink Water Reminder started!!")
print("Press Ctrl+C to exit\n")

try:
    while True:
        schedule.run_pending()
        time.sleep(60)

except KeyboardInterrupt :
    print("\nReminder stopped.")
    