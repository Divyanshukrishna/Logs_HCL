from collections import Counter, defaultdict

def analyze_logs(file_name="logs_large_1000.txt"):
    total_logs = 0
    level_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    error_messages = []
    user_error_count = defaultdict(int)

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

            # Handle empty file
            if not lines:
                print("Log file is empty.")
                return

            for line in lines:
                parts = line.strip().split()

                # Skip invalid lines
                if len(parts) < 6:
                    continue

                total_logs += 1

                date = parts[0]
                time = parts[1]
                level = parts[2]
                user_id = parts[4]
                message = " ".join(parts[5:])

                # Count log levels
                if level in level_count:
                    level_count[level] += 1

                # Error-specific tracking
                if level == "ERROR":
                    error_messages.append(message)
                    user_error_count[user_id] += 1

        # Calculate error percentage
        error_percentage = (
            (level_count["ERROR"] / total_logs) * 100
            if total_logs > 0 else 0
        )

        # Most frequent error
        most_frequent_error = "No Errors Found"
        if error_messages:
            most_frequent_error = Counter(error_messages).most_common(1)[0][0]

        # User with highest errors
        highest_error_user = "None"
        if user_error_count:
            highest_error_user = max(user_error_count, key=user_error_count.get)

        # Generate Report
        print("\n------ SYSTEM REPORT ------\n")
        print(f"Total Logs: {total_logs}")
        print(f"INFO: {level_count['INFO']}")
        print(f"WARNING: {level_count['WARNING']}")
        print(f"ERROR: {level_count['ERROR']}")
        print(f"\nError Percentage: {error_percentage:.2f}%\n")
        print("Most Frequent Error:")
        print(most_frequent_error)
        print("\nUser With Highest Errors:")
        print(f"User {highest_error_user}")

    except FileNotFoundError:
        print("Error: logs_large_1000.txt file not found.")


# Run the analyzer
analyze_logs()