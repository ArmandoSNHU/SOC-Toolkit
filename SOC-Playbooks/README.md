# 📋 SOC Playbook Generator

A command-line tool that generates structured incident response playbooks based on common SOC scenarios.

---

## 🔧 What It Does

- Prompts the user for:
  - Incident type (Phishing, Malware, Data Exfiltration)
  - Analyst name
  - Notes
- Outputs a Markdown `.md` file with:
  - Timestamp
  - Analyst details
  - Action steps for that incident type
  - Custom notes section

---

## ✅ Supported Incident Types

- **Phishing**
- **Malware**
- **Data Exfiltration**

Each one includes a pre-filled list of response steps based on best practices.

---

## 🛠 How to Use

1. Run the script:
   ```bash
   python3 playbook_generator.py
   ```

2. Enter the required info when prompted

3. Your playbook will be saved as:
   ```
   phishing_playbook_20250406_202501.md
   ```

---

## 📁 Files

- `playbook_generator.py` — main Python script
- `*.md` — generated Markdown playbooks

---

## 💡 Ideas for Future Versions

- Export to PDF or HTML
- GUI version with dropdowns
- Add more incident types
- Integrate with alert/ticket system

---

## 👨‍💻 Author

Created by **Armando Gomez**  
Part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

---
