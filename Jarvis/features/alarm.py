import time

def set_alarm(alarm_time):
    current_time = time.strftime('%H:%M')  # Get the current time in HH:MM format
    while current_time != alarm_time:
        current_time = time.strftime('%H:%M')  # Update the current time
        time.sleep(1)  # Check every second if the alarm time has been reached

    print("Alarm! It's time!")

# Example usage:
alarm_time = '10:30'  # Set the alarm time
set_alarm(alarm_time)
