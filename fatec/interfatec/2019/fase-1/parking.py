from datetime import timedelta

times = [
    "9 0 10 0",
    "7 0 8 0",
]


entry_times = []
exit_times = []

for car_time in times:
    hour_entry, minute_entry, hour_exit, minute_exit = car_time.split()
    entry_times.append((int(hour_entry), int(minute_entry)))
    exit_times.append((int(hour_exit), int(minute_exit)))

entry_times.sort()
exit_times.sort(reverse=True)

difference = timedelta(hours=exit_times[0][0], minutes=exit_times[0][1]) - timedelta(
    hours=entry_times[0][0], minutes=entry_times[0][1]
)

print(int(difference.seconds / 60))
