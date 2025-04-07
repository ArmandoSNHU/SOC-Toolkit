# 📝 Incident Report Generator

A command-line tool that helps SOC analysts quickly generate clean, structured incident reports based on analyst input.

---

## 🔍 What It Does

- Prompts the user to fill out key incident details:
  - Analyst name
  - Title
  - Affected system
  - Attack vector
  - IOCs
  - Summary
  - Response steps
- Automatically saves the report with a timestamped filename
- Output format: `.txt`

---

## 📁 Files

- `incident_report_generator.py` — main script
- `incident_report_YYYYMMDD_HHMMSS.txt` — sample generated report(s)

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python3 incident_report_generator.py
   ```

2. Answer the prompts

3. Your report will be saved in the same folder:
   ```
   incident_report_20250406_193000.txt
   ```

---

## 💡 Future Plans

- Add markdown output format
- Option to save reports in a dedicated folder
- Export as PDF or HTML
- GUI version (Tkinter)

---

## 👨‍💻 Author

Built by Armando Gomez as part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

