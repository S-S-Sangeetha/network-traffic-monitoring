# 1. The file we want to analyze
log_file = "network_logs.txt"

print("[*] Starting Network Traffic Analysis...")
print("-" * 50)

suspicious_ip = "10.0.0.45"
alert_count = 0

# 2. Open the log file and read it line by line
with open(log_file, mode='r') as file:
    for line in file:
        
        # 3. Look for HTTP and DNS traffic
        if "HTTP" in line or "DNS" in line:
            
            # 4. Check if the traffic is from the suspicious IP
            if suspicious_ip in line:
                print(f"[!] ALERT: Suspicious traffic detected -> {line.strip()}")
                alert_count += 1
            else:
                print(f"[+] Normal traffic -> {line.strip()}")

print("-" * 50)
print(f"[+] Analysis complete. Found {alert_count} suspicious events from {suspicious_ip}.")
