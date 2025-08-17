# nmap_scanner.py
import nmap
import json

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-sV -O")
    results = {}
    for host in nm.all_hosts():
        results[host] = {
            "state": nm[host].state(),
            "protocols": {}
        }
        for proto in nm[host].all_protocols():
            results[host]["protocols"][proto] = nm[host][proto]
    return results

if __name__ == "__main__":
    target = "scanme.nmap.org"
    report = scan_network(target)
    print(json.dumps(report, indent=2))
