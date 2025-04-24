import pywhatkit as kit
import time
import datetime

# Replace with your WhatsApp Group ID
GROUP_ID = "LeSBKvXjlUjGegGsMn3ygp"  # Example: "ABCD123EFGH567"

def wait_until_start():
    """Wait until exactly 12:10 PM to start sending messages."""
    while True:
        now = datetime.datetime.now()
        if now.hour == 12 and now.minute == 12:
            break
        print(f"Waiting... Current Time: {now.strftime('%H:%M:%S')}")
        time.sleep(1)  # Check every 5 seconds

def send_message():
    """Send a message every minute after 12:10 PM."""
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")  # Format: HH:MM
        message = f"⏰ {current_time} - Time Update!"

        try:
            kit.sendwhatmsg_to_group_instantly(GROUP_ID, message)  # Send instantly
            print(f"Message sent at {current_time}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(60)  # Wait exactly 1 minute

if __name__ == "__main__":
    wait_until_start()  # Wait until 12:10 PM
    send_message()  # Start sending messages every minute