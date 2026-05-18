# SOC Toolkit

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Use Case](https://img.shields.io/badge/Use%20Case-SOC%20Training-7c3aed)](#included-tools)
[![Data](https://img.shields.io/badge/Data-Sample%20Logs-informational)](#safety-notes)

SOC Toolkit is a collection of Python command-line utilities that model common Security Operations Center workflows: log monitoring, incident timeline building, IOC matching, detection rule testing, incident reporting, playbook generation, and PDF export.

The project is intended for training, portfolio demonstration, and local lab use. It uses sample logs and local text files, not production telemetry.

## Included Tools

| Tool | Purpose | Folder |
| --- | --- | --- |
| Log Watcher | Monitors a log file for suspicious keywords and writes alerts | `Log-Watcher/` |
| Event Timeline Generator | Converts log entries into a timeline for incident review | `Event-Timeline-Generator/` |
| Incident Report Generator | Produces structured incident reports from analyst prompts | `Incident-Report-Generator/` |
| SOC Playbook Generator | Creates Markdown playbooks for common incident types | `SOC-Playbooks/` |
| Threat Rule Engine | Matches logs against local detection rules and severity labels | `Threat-Rule-Engine/` |
| IOC Lookup Tool | Compares submitted indicators against a local threat intel list | `IOC-Lookup/` |
| PDF Report Exporter | Converts text incident reports into PDF artifacts | `PDF-Report-Exporter/` |
| SIEM Log Feeder | Generates sample log events for SIEM-style testing | `SIEM-Log-Feeder/` |

## Quick Start

Run the menu dashboard from the repository root:

```powershell
python main.py
```

The dashboard provides numbered access to the individual tools.

## Example Workflows

### Investigate A Sample Authentication Event

```powershell
python Event-Timeline-Generator\timeline_generator.py
python Threat-Rule-Engine\rule_engine.py
python Incident-Report-Generator\incident_report_generator.py
```

### Check Indicators Against Local Threat Intelligence

```powershell
python IOC-Lookup\ioc_lookup.py
```

### Generate A Playbook

```powershell
python SOC-Playbooks\playbook_generator.py
```

## Repository Structure

```text
SOC-Toolkit/
├── Event-Timeline-Generator/
├── IOC-Lookup/
├── Incident-Report-Generator/
├── Log-Watcher/
├── PDF-Report-Exporter/
├── SIEM-Log-Feeder/
├── SOC-Playbooks/
├── Sample-Investigation/
├── Threat-Rule-Engine/
├── main.py
└── README.md
```

## Safety Notes

- Use lab logs and sample indicators only.
- Do not commit real incident data, customer logs, IP addresses from sensitive environments, or proprietary detection content.
- Validate generated reports before sharing them externally.
- Treat tool output as analyst support, not as a replacement for investigation.

## Skills Demonstrated

- Python CLI scripting
- Log parsing and event normalization
- IOC matching
- Basic detection-rule design
- Incident documentation
- Security playbook writing
- Report artifact generation

## Roadmap

- Add a single non-interactive CLI with subcommands.
- Add unit tests for each parser and rule engine.
- Add structured JSON output for integration with other tools.
- Add sample Sigma-style rule conversion.
- Add README examples for each sub-tool.

## Author

Armando Gomez  
GitHub: [@ArmandoSNHU](https://github.com/ArmandoSNHU)
