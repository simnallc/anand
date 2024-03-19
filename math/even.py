# Define the range for generating even numbers
start = 0
end = 20

# Loop through the range and print even numbers
print("Even numbers from", start, "to", end, "are:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
