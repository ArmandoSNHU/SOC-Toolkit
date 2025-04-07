# ⚠️ Threat Rule Engine

A lightweight Python tool that scans log files for defined threat patterns and flags them with severity levels — simulating the behavior of basic SIEM detection rules.

---

## 🔍 What It Does

- Reads from a log file (`sample.log`)
- Matches each line against a list of built-in detection rules
- Displays matching events with:
  - Timestamp
  - Severity (Info, Medium, High)
  - Matching keyword

---

## 🧠 Why This Project Matters

This tool mimics basic rule logic found in enterprise SIEM platforms like Splunk, Sentinel, and QRadar — making it a great showcase for SOC and detection engineering skill sets.

---

## ⚙️ How to Use

1. Ensure `sample.log` contains your test logs.
2. Run the script:
   ```bash
   python3 rule_engine.py
   ```

3. Example log entry:
   ```
   Apr 06 12:01:45 sshd[12345]: Failed password for invalid user admin from 10.0.0.1 port 22
   ```

4. Expected output:
   ```
   [Medium] Apr 06 12:01:45 → Failed password detected:
       sshd[12345]: Failed password for invalid user admin from 10.0.0.1 port 22
   ```

---

## 🧾 Rules in This Version

| Keyword            | Severity |
|--------------------|----------|
| Failed password    | Medium   |
| Accepted password  | Info     |
| sudo:              | High     |
| Blocked IP         | High     |

---

## 🚀 Future Features (Optional)

- Load rules from external `.json` or `.yaml` files
- Add support for regex rules
- Write alerts to `alerts.log`
- Real-time log tailing support

---

## 👨‍💻 Author

Created by **Armando Gomez**  
Part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

---
