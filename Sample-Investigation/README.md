# 🕵️‍♂️ Sample SOC Investigation Case

This folder contains a full mock investigation case performed using the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit), demonstrating a realistic security incident workflow from detection to reporting.

---

## 🔍 Scenario Overview

On April 6, 2025, multiple failed SSH login attempts were detected, followed by a successful root login and privilege escalation using `sudo`. The source IP `10.0.0.66` was identified as hostile and later blocked.

---

## 📂 Contents

| File                        | Description                                |
|-----------------------------|--------------------------------------------|
| `sample_auth.log`           | Simulated Linux system log                 |
| `timeline.txt`              | Chronological breakdown of events          |
| `incident_report.txt`       | Written summary of findings and response   |
| `incident_report.pdf`       | Clean export of the report in PDF format   |
| `malware_playbook.md`       | Response actions based on SOC procedure    |
| `README.md`                 | This file – summary of the case            |

---

## 🚨 Key IOCs

- **Source IP:** `10.0.0.66`
- **Behavior:** Brute force SSH → Root access → `sudo` escalation
- **System Affected:** `ubuntu-lab`

---

## 🧪 Workflow Steps

1. **Log Parsing** — `sample_auth.log` flagged by Log Watcher
2. **Timeline Creation** — Event-Timeline-Generator produced `timeline.txt`
3. **Incident Reporting** — Report generated via CLI tool
4. **PDF Export** — Report converted to `incident_report.pdf`
5. **Playbook Used** — Pre-defined Malware Playbook followed for response

---

## ✅ Response Summary

- Attacker IP `10.0.0.66` blocked at perimeter firewall
- Root credentials rotated on affected system
- System integrity reviewed and logs archived
- Timeline and report generated and submitted

---

## 👨‍💻 Analyst

**Armando Gomez**  
Created as part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

---
