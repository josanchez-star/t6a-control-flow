# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start

interval = 15  # minutes between checks

for check in range(1, 11):
    # Calculate the minutes after shift start for this check
    minutes = check * interval
    # Print the check time
    print(f"Check {check}: {minutes} minutes after shift start")
    # Move to the next check