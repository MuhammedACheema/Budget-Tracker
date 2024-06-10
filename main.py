import csv

# Lists to store data
Date = []
Place = []
SpentAmount = []
Category = []

# List of CSV file names
csv_files = ['January.csv', 'February.csv', 'March.csv', 'April.csv', 'May.csv']

# Loop through each file and read data
for file_name in csv_files:
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 4:  # Ensure the row has enough elements
                Date.append(row[0])
                Place.append(row[1])
                SpentAmount.append(row[2])
                Category.append(row[3])

# Function to calculate the total amount
def calculate_total(total):
    tot = [float(i) for i in total]
    tots = sum(tot)
    return tots

# Function to calculate the average amount
def calculate_avg(avg):
    total = calculate_total(avg)
    avg_total = total / len(avg)
    return avg_total

#Used ChatGPT to help create this function
# Calculate the total amount spent on each category
def calculate_total_by_category(categories, amounts):
    totals_by_category = {}
    for i in range(len(categories)):
        category = categories[i]
        amount = float(amounts[i])
        if category not in totals_by_category:
            totals_by_category[category] = 0.0
        totals_by_category[category] += amount
    return totals_by_category

# Calculate the totals by category
totals_by_category = calculate_total_by_category(Category, SpentAmount)

# Print the totals by category
for category, total in totals_by_category.items():
    print(f"Total spent on {category}: ${total:.2f}")

# Print total and average spent amount (optional)
print(f"Total spent amount: ${calculate_total(SpentAmount):.2f}")
print(f"Average spent amount: ${calculate_avg(SpentAmount):.2f}")
