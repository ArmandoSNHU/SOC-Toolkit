from datetime import datetime

LOG_FILE = "sample_auth.log"
OUTPUT_FILE = "timeline.txt"

KEYWORDS = {
    "Failed password": "Unauthorized Login Attempt",
    "Accepted password": "Successful Login",
    "sudo:": "Privilege Escalation",
    "Blocked IP": "Firewall Action"
}

def generate_timeline():
    with open(LOG_FILE, "r", encoding="utf-8") as log, open(OUTPUT_FILE, "w") as timeline:
        print("🔍 Building security event timeline...\n")
        for line in log:
            for keyword, label in KEYWORDS.items():
                if keyword in line:
                    timestamp = line[:15]
                    timeline.write(f"{timestamp} — {label} — {line.strip()}\n")
    print(f"✅ Timeline written to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_timeline()
