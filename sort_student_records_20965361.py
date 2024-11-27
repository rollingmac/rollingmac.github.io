# Author: Yeung Pok
# Student ID: 20965361

import csv

# Function to compare records
def compare(record1, record2):
    if record1[1] < record2[1]:
        return True
    elif record1[1] == record2[1]:
        if record1[0] < record2[0]:
            return True
        elif record1[0] == record2[0]:
            return record1[2] < record2[2]
    return False

# Function to perform bubble sort
def bubble_sort(records):
    n = len(records)
    for i in range(n):
        for j in range(0, n-i-1):
            if not compare(records[j], records[j+1]):
                # Swap if the current record is greater than the next
                records[j], records[j+1] = records[j+1], records[j]

# Read records from CSV
with open('student_records.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    records = [row for row in reader]

# Sort the records using bubble sort
bubble_sort(records)

# Write sorted records to a new CSV file
with open('student_records_sorted.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write header
    writer.writerows(records)  # Write sorted records
