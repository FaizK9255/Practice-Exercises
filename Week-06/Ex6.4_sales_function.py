

employees = ['John', 'Sarah', 'Michael', 'Jennifer', 'David']
sales = [5200, 6800, 4500, 7200, 5800]

def calculate_total(sales):
    total = 0

    for sale in sales:
        total += sale

    return total 


def calculate_average(total, number_of_employees):
    average = total / number_of_employees

    return average


total = calculate_total(sales)

print(f"Total Monthly Sales: ${total:,.2f}")

count = len(employees)

average = calculate_average(total, count)

print(f'Average Sales per Employee: ${average:,.2f}')

