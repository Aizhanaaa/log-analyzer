from collections import defaultdict

log_file = "log.txt"
ip_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line or "401" in line:
            parts = line.split()
            ip = parts[0]
            ip_attempts[ip] += 1

print("Suspicious activity detected:\n")

for ip, count in ip_attempts.items():
    if count > 3:
        print(f"{ip} - {count} failed attempts")
