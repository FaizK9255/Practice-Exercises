import statistics

days = [
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]

sales = [1250, 1480, 1100, 1650, 1850,
1420, 1700, 1300, 2100, 1950]

for i in range(len(days)):
    print(days[i], sales[i])

print(f"{'DESCRIPTIVE CALCULATIONS':^30}")
print("-" * 30)

labels = ["Mean", "Median", "Mode", "Standard Deviation", 
"Sum", "Minimum", "Maximum"]

calculations = [
    statistics.mean(sales),
    statistics.median(sales),
    statistics.mode(sales),
    statistics.stdev(sales),
    sum(sales),
    min(sales),
    max(sales)
]

for i in range(len(calculations)):
    print(labels[i], calculations[i])


if sales >= 1800:
    print("Excellent")

elif sales >= 1500:
    print("Good")

elif sales >= 1200:
    print("Average")

else:
    print("Needs Improvement") 