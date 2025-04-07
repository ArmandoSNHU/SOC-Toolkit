# 🧾 PDF Report Exporter

This tool converts plaintext incident reports into polished, printable PDF files. It’s designed to work alongside the [Incident Report Generator](../Incident-Report-Generator) in the SOC Toolkit, creating professional documentation for security incidents.

---

## ✅ What It Does

- Takes an existing `.txt` incident report
- Converts it to a clean, formatted `.pdf`
- Automatically timestamps the PDF filename
- Ideal for submitting reports to management or archiving

---

## 📁 File Structure

```
PDF-Report-Exporter/
├── pdf_exporter.py            # Main script
├── incident_report_sample.txt # Sample input (optional)
└── incident_report_YYYYMMDD.pdf  # Output
```

---

## 🚀 How to Use

1. Ensure you have a `.txt` report to convert.
2. Run the tool:
   ```bash
   python3 pdf_exporter.py
   ```
3. When prompted, enter your report file (e.g. `incident_report_sample.txt`)
4. Your `.pdf` will be generated in the same folder.

---

## 🖨️ Example Output

From this:
```
Analyst: Armando Gomez
Incident Title: SSH Brute Force
Date: 2025-04-06
...
```

To this:
```
incident_report_20250406_173532.pdf ✅
```

---

## 📦 Requirements

- Python 3.x
- fpdf (`pip install fpdf`)

---

## 👨‍💻 Author

Created by **Armando Gomez**  
Part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

---
