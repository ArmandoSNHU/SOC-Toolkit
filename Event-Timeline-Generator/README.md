# 📅 Event Timeline Generator

This tool reads system log files and generates a timeline of security events.

## 🚀 Usage

1. Run: `python3 timeline_generator.py`
2. Output: `timeline.txt` will be created from `sample_auth.log`

## 🧠 Detection Keywords

- Failed password → Unauthorized Login Attempt  
- Accepted password → Successful Login  
- sudo: → Privilege Escalation  
- Blocked IP → Firewall Action  

Part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)
