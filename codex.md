# Codex Guide

## Project Purpose

SOC Toolkit is a Python-based cybersecurity lab and portfolio repository. It should show practical SOC analyst workflows using sample logs, sample indicators, and generated reports.

## Repository Layout

- `main.py` - interactive dashboard.
- `Log-Watcher/` - keyword log monitoring.
- `Event-Timeline-Generator/` - timeline generation from logs.
- `Incident-Report-Generator/` - incident report creation.
- `SOC-Playbooks/` - Markdown playbook generation.
- `Threat-Rule-Engine/` - local detection rule matching.
- `IOC-Lookup/` - local IOC matching.
- `PDF-Report-Exporter/` - text-to-PDF reporting.
- `SIEM-Log-Feeder/` - generated sample logs.
- `Sample-Investigation/` - example output artifacts.

## Common Commands

Run the dashboard:

```powershell
python main.py
```

Run individual tools from the repository root:

```powershell
python Log-Watcher\log_watcher.py
python Event-Timeline-Generator\timeline_generator.py
python Threat-Rule-Engine\rule_engine.py
python IOC-Lookup\ioc_lookup.py
python SOC-Playbooks\playbook_generator.py
```

## Editing Rules

- Do not commit real security logs, production incident reports, customer data, credentials, or private IOCs.
- Keep tool READMEs aligned with actual command names and generated files.
- Prefer structured outputs where possible: JSON, CSV, Markdown, or normalized text.
- If adding dependencies, create and document a `requirements.txt`.
- If changing parsing behavior, add sample input and expected output.

## Verification

Manually run changed tools against their included sample files. If tests are added later, document the test command here and in the root README.

