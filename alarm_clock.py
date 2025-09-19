from datetime import datetime   
from playsound import playsound
import os
import time

alarm_time = input("Enter alarm time (HH:MM:SSAM/PM): ").strip()
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[8:].upper()

if not os.path.exists('audio.mp3'):
    print("❌ Audio file 'audio.mp3' not found!")
    exit()

print("⏰ Alarm is set...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if (alarm_period == current_period and
        alarm_hour == current_hour and
        alarm_minute == current_minute and
        alarm_seconds == current_seconds):
        print("🔔 Wake Up!")
        playsound('audio.mp3')
        break

    time.sleep(1)  # Don't overload CPU
