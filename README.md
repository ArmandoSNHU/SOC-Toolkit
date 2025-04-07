# 🛡️ SOC Toolkit

A collection of hands-on tools built to simulate key workflows and tasks performed by SOC (Security Operations Center) analysts. This repo is designed to demonstrate real-world detection, monitoring, and incident response skills.

---

## 📦 Tools Included

### 🔍 Log Watcher
Monitors a log file in real time for suspicious keywords like `Failed password`, `sudo`, or `unauthorized`.  
📁 `Log-Watcher/`

**Features:**
- Watches `example.log` for activity
- Triggers alerts in terminal
- Logs alerts to `alerts.log`

---

### 🗂️ Event Timeline Generator
Parses a log file and builds a timestamped incident timeline for investigation purposes.  
📁 `Event-Timeline-Generator/`

**Features:**
- Scans `sample.log` for login attempts and sudo usage
- Writes a structured timeline to `timeline.txt`
- Easy to expand with new patterns

---

## 🎯 Why This Repo Exists

Built to showcase real-world SOC skills for detection engineering and Tier 1–2 security analyst roles. These tools simulate the kind of day-to-day tasks involved in:
- Monitoring endpoint/system logs
- Creating detection rules
- Investigating alerts
- Building incident reports

---

## 🚀 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/ArmandoSNHU/SOC-Toolkit.git
   cd SOC-Toolkit
   ```

2. Navigate into any tool directory and follow the included instructions:
   ```bash
   cd Log-Watcher
   python3 log_watcher.py
   ```

---

## 📌 Coming Soon

- ✅ Threat Rule Engine (SIEM-style pattern matching)
- ✅ Incident Report Generator
- ✅ Realistic log datasets for analysis
- ✅ Windows Event Log parsing

---

## 🔐 Built With

- Python 3.x
- VS Code
- Logs inspired by `/var/log/auth.log` and SSHD output

---

## 🙋‍♂️ Author

Made by **Armando Gomez**  
📍 GitHub: [ArmandoSNHU](https://github.com/ArmandoSNHU)

---
