import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
INPUT_FILE = "ioc_input.txt"
THREAT_FEED = "threat_intel.txt"
HITS_FILE = "ioc_hits.txt"

def load_threat_feed():
    try:
        with open(THREAT_FEED, "r") as f:
            return set(line.strip() for line in f.readlines())
    except FileNotFoundError:
        print("⚠️ Threat feed not found, continuing without it.")
        return set()

def check_abuseipdb(ip):
    if not ABUSEIPDB_API_KEY:
        return {"error": "API key not found. Make sure .env is set."}

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()["data"]
            return {
                "abuseScore": data["abuseConfidenceScore"],
                "country": data.get("countryCode", "N/A"),
                "isp": data.get("isp", "N/A"),
                "usageType": data.get("usageType", "N/A"),
                "lastReported": data.get("lastReportedAt", "N/A")
            }
        else:
            return {"error": f"Lookup failed: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request error: {e}"}

def run_lookup():
    threat_feed = load_threat_feed()

    with open(INPUT_FILE, "r") as f, open(HITS_FILE, "w") as out:
        for line in f:
            ioc = line.strip()
            if not ioc:
                continue

            print(f"\n🔍 Checking: {ioc}")
            in_feed = ioc in threat_feed

            if in_feed:
                out.write(f"{ioc} — MATCHED in threat feed\n")
                print(f"✅ {ioc} found in threat feed.")
            else:
                print(f"❌ {ioc} not in local threat feed.")

            if "." in ioc and ioc.count(".") == 3:  # Simple IP check
                result = check_abuseipdb(ioc)
                if "error" in result:
                    print(f"⚠️ {result['error']}")
                else:
                    out.write(f"{ioc} — Abuse Score: {result['abuseScore']} | Country: {result['country']} | ISP: {result['isp']}\n")
                    print(f"🌐 AbuseIPDB: Score {result['abuseScore']}/100 | Country: {result['country']} | ISP: {result['isp']}")

if __name__ == "__main__":
    run_lookup()
