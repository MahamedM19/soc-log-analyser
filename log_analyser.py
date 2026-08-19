failed_logins = 0

with open("security.log", "r") as file:
    for line in file:
        if "LOGIN_FAILED" in line:
            failed_logins += 1

print("There has been", failed_logins, "failed login attempts")
