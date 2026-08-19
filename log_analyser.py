failed_logins = 0
failed_ips = {}

with open("security.log", "r") as file:
    for line in file:
        if "LOGIN_FAILED" in line:
            failed_logins += 1

            parts = line.split()
            ip_address = parts[4].replace("ip=", "")

            if ip_address in failed_ips:
                failed_ips[ip_address] += 1
            else:
                failed_ips[ip_address] = 1

print("There has been", failed_logins, "failed login attempts")

print("\nFailed logins by IP:")

for ip, count in failed_ips.items():
    print(ip, ":", count)
