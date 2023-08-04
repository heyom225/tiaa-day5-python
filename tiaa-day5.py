#Create one empty list add prime numbers..........

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in range(2, 51) if is_prime(num)]
print(prime_numbers)

# Print user input table

num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
table = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        data = input(f"Enter data for row {i+1}, column {j+1}: ")
        row.append(data)
    table.append(row)
for row in table:
    for data in row:
        print(data, end="\t")
    print()
   
#  Print palindrome string taking input as string

a1=input("Enter a string: ")
print(f"The string {a1} is palindrome: {a1==a1[::-1]}")

# Take input as string and reverse it

print(f"Reversed string: {input('Enter a string: ')[::-1]}")