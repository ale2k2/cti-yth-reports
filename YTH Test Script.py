import csv
import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:\\Users\\alexb\\Downloads\\YTH Attendance 6.20-8.8 - Check-Ins Report.csv"

# Read CSV
df = pd.read_csv(file_path)

# Get date columns (after first 4 metadata columns)
date_columns = df.columns[4:]

# Count attendance per date
attendance_counts = df[date_columns].apply(lambda col: col.astype(str).str.lower() == 'true').sum()

# Generate evenly spaced Friday labels starting July 18, 2025
start_date = pd.to_datetime('2025-07-18')
num_weeks = len(date_columns)
even_fridays = pd.date_range(start=start_date, periods=num_weeks, freq='W-FRI')

# Treat x-axis as simple positions (0, 1, 2...) for even spacing
x_positions = range(num_weeks)

plt.figure(figsize=(10, 6))
plt.bar(x_positions, attendance_counts.values, color='skyblue', edgecolor='black')
plt.title('Weekly CTI YTH Attendance')
plt.xlabel('Friday YTH Events')
plt.ylabel('Number of Attendees')
plt.grid(axis='y')

# Replace numeric ticks with our Friday labels
plt.xticks(ticks=x_positions, labels=[d.strftime('%b %d, %Y') for d in even_fridays], rotation=45)

plt.tight_layout()
plt.show()

# Convert attendance columns to boolean
attendance_bool = df[date_columns].apply(lambda col: col.astype(str).str.lower() == 'true')

# Total events attended per student
df['TotalAttendance'] = attendance_bool.sum(axis=1)

# Average attendance per grade
avg_attendance_by_grade = df.groupby('Grade')['TotalAttendance'].mean()

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(avg_attendance_by_grade, labels=avg_attendance_by_grade.index,
        autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
plt.title('Average Weekly Attendance by Grade')
plt.axis('equal')
plt.tight_layout()
plt.show()