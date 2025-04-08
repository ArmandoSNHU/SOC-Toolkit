import os
import random
from datetime import datetime, timedelta

# Output directory
OUTPUT_DIR = "generated_logs"
LOG_FILE = os.path.join(OUTPUT_DIR, "auth.log")

# Sample usernames and IPs for brute force
usernames = ["admin", "root", "jdoe", "backup", "devops"]
source_ips = ["192.168.1." + str(i) for i in range(100, 120)]

# Make sure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def random_timestamp(start, count):
    """Generate a list of timestamps starting from `start` spaced ~1-2 mins apart"""
    return [start + timedelta(minutes=random.randint(1, 2) * i) for i in range(count)]

def generate_brute_force_log_entries(num_entries=10):
    """Generate failed login attempts like you'd see in /var/log/auth.log"""
    start_time = datetime.now() - timedelta(hours=1)
    timestamps = random_timestamp(start_time, num_entries)

    logs = []
    for i in range(num_entries):
        time_str = timestamps[i].strftime("%b %d %H:%M:%S")
        ip = random.choice(source_ips)
        user = random.choice(usernames)
        line = f"{time_str} kali sshd[99999]: Failed password for invalid user {user} from {ip} port 22 ssh2"
        logs.append(line)
    return logs

def write_logs(logs):
    with open(LOG_FILE, "w") as f:
        for line in logs:
            f.write(line + "\n")
    print(f"✅ {len(logs)} log entries written to {LOG_FILE}")

if __name__ == "__main__":
    print("🔧 Generating simulated brute-force logs...")
    logs = generate_brute_force_log_entries(15)
    write_logs(logs)
