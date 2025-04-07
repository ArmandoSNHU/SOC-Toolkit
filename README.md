# 🛡️ SOC Toolkit

A collection of hands-on tools built by Armando Gomez to simulate workflows performed by Security Operations Center (SOC) analysts.  
Each tool focuses on real-world detection, response, and documentation techniques — all built in Python and accessible via a single CLI dashboard.

---

## 🚀 Run the Toolkit

Use the main dashboard to launch any tool from a menu:

```bash
python main.py
```

This will show:

```
=== 🛡️ SOC TOOLKIT MAIN MENU ===

1. Log Watcher
2. Event Timeline Generator
3. Incident Report Generator
4. SOC Playbook Generator
5. Threat Rule Engine
6. IOC Lookup Tool
7. PDF Report Exporter
0. Exit
```

---

## 🧰 Included Tools

### 1️⃣ Log Watcher
Real-time keyword-based log monitor  
📁 [`Log-Watcher`](./Log-Watcher)

### 2️⃣ Event Timeline Generator
Parses logs into timestamped IR timelines  
📁 [`Event-Timeline-Generator`](./Event-Timeline-Generator)

### 3️⃣ Incident Report Generator
Prompt-based CLI tool to document incidents  
📁 [`Incident-Report-Generator`](./Incident-Report-Generator)

### 4️⃣ SOC Playbook Generator
Builds Markdown playbooks for Phishing, Malware, etc.  
📁 [`SOC-Playbooks`](./SOC-Playbooks)

### 5️⃣ Threat Rule Engine
Scans logs for matches to detection rules with severity  
📁 [`Threat-Rule-Engine`](./Threat-Rule-Engine)

### 6️⃣ IOC Lookup Tool
Flags IOCs using a local threat intel list  
📁 [`IOC-Lookup`](./IOC-Lookup)

### 7️⃣ PDF Report Exporter
Converts `.txt` reports into printable `.pdf` files  
📁 [`PDF-Report-Exporter`](./PDF-Report-Exporter)

---

## 🧠 Why This Exists

This toolkit was built to:
- Simulate the day-to-day work of SOC analysts
- Help learn detection engineering concepts
- Demonstrate real-world technical workflows in cybersecurity

---

## 👨‍💻 Author

**Armando Gomez**  
GitHub: [ArmandoSNHU](https://github.com/ArmandoSNHU)

---
