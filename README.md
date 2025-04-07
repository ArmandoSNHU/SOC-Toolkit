# 🛡️ SOC Toolkit

A collection of hands-on tools built by Armando Gomez to simulate workflows performed by Security Operations Center (SOC) analysts.  
Each tool focuses on real-world detection, response, and documentation techniques — built entirely in Python and easy to run from the command line.

---

## 🚀 Included Tools

### 🔍 [Log Watcher](./Log-Watcher)
Real-time log monitoring tool that detects suspicious activity by scanning for defined keywords.

- Monitors a live log file (e.g. `example.log`)
- Triggers alerts on things like `Failed password`, `sudo`, `unauthorized`
- Alerts are written to a terminal and `alerts.log`

---

### 🗂️ [Event Timeline Generator](./Event-Timeline-Generator)
Parses log files and builds timestamped incident timelines — useful for investigations and IR documentation.

- Scans logs for login attempts, sudo usage, and more
- Generates a timeline in `timeline.txt`
- Helps reconstruct event flow for IR reports

---

### 📝 [Incident Report Generator](./Incident-Report-Generator)
Creates a structured incident report from SOC analyst prompts.

- Input: Title, affected system, attack vector, IOCs, response steps
- Output: A clean `.txt` report with all details
- Helps SOC analysts document incidents fast and consistently

---

### 📋 [SOC Playbook Generator](./SOC-Playbooks)
Builds Markdown-based response playbooks for phishing, malware, and data exfiltration incidents.

- CLI tool with pre-built response steps for each incident type
- Saves results as `*.md` files
- Ideal for documenting IR procedures

---

### ⚠️ [Threat Rule Engine](./Threat-Rule-Engine)
A rule-based alert system that scans logs and flags events based on severity.

- Keywords are mapped to severity levels: Info / Medium / High
- Scans `sample.log` for known patterns
- Simulates lightweight SIEM detection logic

---

## 🎯 Why This Exists

This toolkit is designed to:
- Practice key SOC workflows using Python
- Document skills for SOC, IR, and cybersecurity job applications
- Show real-world understanding of logs, alerts, playbooks, and threat detection

---

## 🧰 Tech Stack

- Python 3.x
- Basic file I/O and CLI-based tools
- Markdown for playbooks and reporting

---

## 👨‍💻 Author

**Armando Gomez**  
GitHub: [ArmandoSNHU](https://github.com/ArmandoSNHU)  
Built with ❤️ as a learning and portfolio project

---

