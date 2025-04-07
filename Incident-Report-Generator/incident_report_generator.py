from datetime import datetime

def get_input(prompt):
    return input(f"{prompt}: ").strip()

def generate_report():
    print("\n=== Incident Report Generator ===\n")

    report_data = {
        "Analyst Name": get_input("Your name"),
        "Incident Title": get_input("Incident title"),
        "Date/Time of Detection": get_input("When was it detected?"),
        "Affected System": get_input("Which system was affected?"),
        "Attack Vector": get_input("How did it happen? (e.g. phishing, brute force)"),
        "Indicators of Compromise": get_input("Any IOCs? (IPs, hashes, domains)"),
        "Summary": get_input("Brief summary of the incident"),
        "Remediation Steps": get_input("How did you respond?")
    }

    filename = f"incident_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("=== INCIDENT REPORT ===\n\n")
        for key, value in report_data.items():
            f.write(f"{key}:\n{value}\n\n")

    print(f"\n✅ Report saved as {filename}")

if __name__ == "__main__":
    generate_report()
