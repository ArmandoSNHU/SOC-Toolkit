def load_file(path):
    with open(path, "r") as f:
        return set(line.strip() for line in f if line.strip())

def lookup_iocs(ioc_file, threat_file):
    iocs = load_file(ioc_file)
    threats = load_file(threat_file)

    print("=== IOC Lookup Tool ===\n")
    print("Suspicious indicators found:\n")

    hits = []
    for ioc in iocs:
        if ioc in threats:
            print(f"⚠️  {ioc} → MATCH FOUND")
            hits.append(ioc)
        else:
            print(f"✅ {ioc} → clean")

    if hits:
        with open("ioc_hits.txt", "w") as f:
            for ioc in hits:
                f.write(ioc + "\n")
        print("\n🚩 Matches written to ioc_hits.txt")
    else:
        print("\n🎉 No malicious IOCs detected.")

if __name__ == "__main__":
    lookup_iocs("ioc_input.txt", "threat_intel.txt")
