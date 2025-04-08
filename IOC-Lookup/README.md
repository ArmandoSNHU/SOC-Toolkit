# 🕵️ IOC Lookup Tool

The IOC (Indicators of Compromise) Lookup Tool allows you to:

- Match indicators (IPs, domains, hashes) against a custom threat feed
- Enrich IPs in real-time using the AbuseIPDB API
- Log and export results to a report file

Part of the [SOC Toolkit](https://github.com/ArmandoSNHU/SOC-Toolkit)

---

## ⚙️ How It Works

1. Load IOCs from `ioc_input.txt`
2. Compare each one against `threat_intel.txt`
3. Enrich IPs with threat reputation data from [AbuseIPDB](https://abuseipdb.com)
4. Save results to `ioc_hits.txt`

---

## 📂 File Structure

```
IOC-Lookup/
├── ioc_lookup.py           # Main script
├── ioc_input.txt           # Input IOCs (IPs, domains, hashes)
├── threat_intel.txt        # Your known threat feed
├── ioc_hits.txt            # Output log file (auto-generated)
├── .env                    # Stores your API key (ignored by Git)
└── README.md
```

---

## ✏️ Input Format

Each line in `ioc_input.txt` should be one IOC:

```
8.8.8.8
10.0.0.5
malicious-domain.com
badfile.exe
```

---

## 🛡️ Sample Output in `ioc_hits.txt`

```
10.0.0.5 — MATCHED in threat feed
8.8.8.8 — Abuse Score: 0 | Country: US | ISP: Google LLC
185.220.101.47 — MATCHED in threat feed
```

---

## 🔐 AbuseIPDB API Setup

To enable live IP enrichment:

1. Sign up at: https://abuseipdb.com
2. Go to: https://abuseipdb.com/account/api and get your key
3. Create a file called `.env` in this folder:

```
ABUSEIPDB_API_KEY=your_key_here
```

> 🚫 This file is ignored by Git to keep your credentials safe.

---

## ✅ Requirements

- Python 3.x
- `requests`  
- `python-dotenv`

Install them with:

```bash
pip install requests python-dotenv
```

---

## 🧠 Use Cases

- Threat hunting
- IOC validation
- Enrichment during incident response
- Quick triage of suspicious IPs/domains

---

## 👨‍💻 Author

**Armando Gomez**  
GitHub: [@ArmandoSNHU](https://github.com/ArmandoSNHU)  

---
