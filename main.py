import os
import subprocess

TOOLS = {
    "1": ("Log Watcher", "Log-Watcher/log_watcher.py"),
    "2": ("Event Timeline Generator", "Event-Timeline-Generator/timeline_generator.py"),
    "3": ("Incident Report Generator", "Incident-Report-Generator/incident_report_generator.py"),
    "4": ("SOC Playbook Generator", "SOC-Playbooks/playbook_generator.py"),
    "5": ("Threat Rule Engine", "Threat-Rule-Engine/rule_engine.py"),
    "6": ("IOC Lookup Tool", "IOC-Lookup/ioc_lookup.py"),
    "7": ("PDF Report Exporter", "PDF-Report-Exporter/pdf_exporter.py")
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear()
        print("=== 🛡️ SOC TOOLKIT MAIN MENU ===\n")
        for key, (label, _) in TOOLS.items():
            print(f"{key}. {label}")
        print("0. Exit")

        choice = input("\nSelect a tool to run: ").strip()

        if choice == "0":
            print("Exiting SOC Toolkit.")
            break
        elif choice in TOOLS:
            label, path = TOOLS[choice]
            print(f"\n▶️ Running {label}...\n")
            subprocess.run(["python", path])
            input("\n[Press Enter to return to menu]")
        else:
            input("❌ Invalid choice. Press Enter to try again.")

if __name__ == "__main__":
    main_menu()
