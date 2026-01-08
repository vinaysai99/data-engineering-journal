import csv
import random
import string
import os
from datetime import datetime, timedelta

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_csv(filename="motel_logs.csv", num_rows=400, num_columns=5):
    """Generates a CSV file with random data."""
    headers = ["guest_id", "check_in_date", "room_number", "guest_name","bill_amount"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(headers)

        # Write the data rows
        for i in range(num_rows):
            # Generate random data for each column
            col1 = i + 1  # Sequential ID
            days_ago = random.randint(0, 365)
            col2 = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
            col3 = random.randint(101, 505)
            col4 = generate_random_string() # Random string name
            col5 = round(random.uniform(50.00, 1500.00), 2)

            # Write the row to the CSV file
            writer.writerow([col1, col2, col3, col4,col5])

    print(f"Successfully generated {filename} with {num_rows} rows.")
    print(f"File saved at: {os.path.abspath(filename)}")


# --- Run the function ---
# You can change the number of rows as needed
generate_random_csv(num_rows=400)
