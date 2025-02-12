import random

def collect_data(num_users):
    data = []
    for _ in range(num_users):
        usage = random.uniform(0, 100)  # Random usage between 0 to 100 GB
        quota = random.uniform(50, 100)  # Random quota between 50 to 100 GB
        data.append((usage, quota))
    return data

if __name__ == "__main__":
    users_data = collect_data(10)
    for i, (usage, quota) in enumerate(users_data):
        print(f"User {i+1} - Usage: {usage} GB, Quota: {quota} GB")
