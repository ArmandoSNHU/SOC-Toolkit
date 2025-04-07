# 🔍 IOC Lookup Tool

A simple Python-based lookup tool that compares a list of IOCs (Indicators of Compromise) against a local threat intelligence feed.  
It flags matches and exports them to a results file for reporting or escalation.

---

## 🧠 What It Does

- Reads a list of IOCs from `ioc_input.txt`
- Compares them against known bad indicators in `threat_intel.txt`
- Flags any matches in the terminal
- Saves matched IOCs to `ioc_hits.txt`

---

## 📂 File Structure

```
IOC-Lookup/
├── ioc_lookup.py         # Main script
├── ioc_input.txt         # Your list of IOCs (IPs, domains, hashes, filenames)
├── threat_intel.txt      # Known malicious indicators
└── ioc_hits.txt          # Output of confirmed matches
```

---

## 🚀 How to Use

1. Edit `ioc_input.txt` with IOCs to check (one per line)
2. Add threat intel to `threat_intel.txt`
3. Run the script:
   ```bash
   python3 ioc_lookup.py
   ```

---

## ✅ Sample Output

```
=== IOC Lookup Tool ===

Suspicious indicators found:

⚠️  10.0.0.5 → MATCH FOUND
✅  8.8.8.8 → clean
⚠️  malicious-domain.com → MATCH FOUND

🚩 Matches written to ioc_hits.txt
```

---

## 🧠 Ideas for Future Versions

- API integration (VirusTotal, AbuseIPDB, AlienVault OTX)
- Hash classification (SHA-256, MD5)
- Output in JSON, CSV, or Markdown formats

---

## 👨‍💻 Author

Created by **Armando Gomez**  
Part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

---
