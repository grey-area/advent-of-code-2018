import utils

guard_sleep_counts = utils.load_data()

# Get the guard who sleeps the most number of minutes, and the count
# for number of times he's slept during each minute.
guard_id, sleep_counts = max(guard_sleep_counts.items(), key=lambda x: x[1].sum())

# Guard ID multiplied by the minute he's slept the most.
print(guard_id * sleep_counts.argmax())
