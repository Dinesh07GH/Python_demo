# datetime_example.py

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Format date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted)

# Extract components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Add 7 days to current date
future = now + timedelta(days=7)
print("Date after 7 days:", future.strftime("%Y-%m-%d"))

# Subtract 30 days from current date
past = now - timedelta(days=30)
print("Date 30 days ago:", past.strftime("%Y-%m-%d"))

# Parse date from string
date_string = "2025-12-25"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date from string:", parsed_date)
