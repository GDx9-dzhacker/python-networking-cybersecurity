# Login Log Analyzer
# Analyzes failed login attempts and detects suspicious IP addresses.


def analyze_logs(filename):
    failed_attempts = {}

    try:
        # Open the log file in read mode
        with open(filename, "r") as file:

            # Read the file line by line
            for line in file:
                ip, status = line.split()

                # Only count failed login attempts
                if status == "LOGIN_FAILED":

                    # If the IP already exists, increase its counter
                    if ip in failed_attempts:
                        failed_attempts[ip] += 1

                    # Otherwise, create a new entry
                    else:
                        failed_attempts[ip] = 1

    except FileNotFoundError:
        print(f"ERROR: File '{filename}' was not found.")
        return

    return failed_attempts


def detect_suspicious_ips(failed_attempts):
    suspicious_ips = 0
    total_failed_attempts = sum(failed_attempts.values())

    print("\n===== LOGIN ANALYSIS =====")
    print(f"Total failed attempts: {total_failed_attempts}")

    print("\n===== SECURITY ALERTS =====")

    # Check every IP and its number of failed attempts
    for ip, attempts in failed_attempts.items():

        # Three or more failed attempts are considered suspicious
        if attempts >= 3:
            suspicious_ips += 1

            print(
                f"\n[ALERT] Suspicious IP: {ip}\n"
                f"Failed attempts: {attempts}"
            )

    print(f"\nSuspicious IPs: {suspicious_ips}")


# ------------------------- MAIN PROGRAM -------------------------

filename = "[enter your file name]"

failed_attempts = analyze_logs(filename)

# Only continue if the file was successfully analyzed
if failed_attempts is not None:
    detect_suspicious_ips(failed_attempts)
