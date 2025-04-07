from datetime import datetime

RULES = {
    "Failed password": "Medium",
    "Accepted password": "Info",
    "sudo:": "High",
    "Blocked IP": "High"
}

LOG_FILE = "sample.log"

def analyze_logs():
    print("=== Threat Rule Engine ===\n")
    with open(LOG_FILE, "r", encoding="utf-8") as log:
        for line in log:
            for keyword, severity in RULES.items():
                if keyword in line:
                    timestamp = " ".join(line.split()[0:3])
                    print(f"[{severity}] {timestamp} → {keyword} detected:\n    {line.strip()}\n")

if __name__ == "__main__":
    analyze_logs()
