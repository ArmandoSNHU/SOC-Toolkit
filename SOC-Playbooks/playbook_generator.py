from datetime import datetime

TEMPLATES = {
    "Phishing": [
        "Identify affected users",
        "Block malicious sender/domain",
        "Reset compromised passwords",
        "Check for lateral movement",
        "Educate users on phishing indicators"
    ],
    "Malware": [
        "Isolate infected system",
        "Collect malware samples (hash, filename)",
        "Run AV scan and remove",
        "Check logs for spread or C2",
        "Restore from backup if needed"
    ],
    "Data Exfiltration": [
        "Identify data accessed or stolen",
        "Block outbound connection",
        "Disable user account if insider threat",
        "Preserve forensic evidence",
        "Report to compliance/legal if required"
    ]
}

def generate_playbook():
    print("=== SOC Playbook Generator ===\n")
    incident_type = input("Incident type (Phishing / Malware / Data Exfiltration): ").strip().title()

    if incident_type not in TEMPLATES:
        print("🚫 Unsupported incident type.")
        return

    analyst = input("Analyst name: ")
    notes = input("Additional notes: ")

    filename = f"{incident_type.lower()}_playbook_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 🛡️ {incident_type} Incident Response Playbook\n\n")
        f.write(f"**Analyst:** {analyst}\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## 📋 Response Steps\n")
        for i, step in enumerate(TEMPLATES[incident_type], 1):
            f.write(f"{i}. {step}\n")
        f.write("\n## 📝 Notes\n")
        f.write(f"{notes}\n")

    print(f"\n✅ Playbook saved as: {filename}")

if __name__ == "__main__":
    generate_playbook()
