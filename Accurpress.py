from fractions import Fraction
from itertools import combinations
from test.test_bisect import Range

# Helper function that takes a float and returns a fractional string representation of that number
def display_fraction(x):
    if (x >= 0 and x < 1):
        return str(Fraction(x))
    else:
        if (x - int(x) == 0):
            f = ""
        else:
            f = Fraction(x - int(x))
        return "%s %s" % (str(int(x)), f)

# Ask for number of numbers, n
while True:
    try:
        n = int(input("Enter the number of numbers: "))
        if isinstance(n, int):
            break
    except ValueError:
        print("Invalid number.")
        
print ("Number of numbers: " + str(n))

# If n = 0, uses test values
if n == 0:
    # Adjust n and numbers for your own purposes
    n = 9
    numbers = [0.75, 1, 1.25, 2.25, 4, 8.5, 17, 34, 75.25]
    print("Using test values:")
    for num in numbers:
        print(display_fraction(num))        
# Otherwise, ask for numbers from user        
else:
    numbers = []
    # Enter numbers one by one
    for i in range(0, n):
        while True:
            try:
                x = float(eval(input("Enter number " + str(i + 1) + ": ")))
                print(str(x))
                if isinstance(x, float):
                    if x > 0:
                        numbers.append(x)
                        print("Added %s to list of numbers" % Fraction(x))
                        break
                    else:
                        print("Positive numbers only.")
            except:
                print("Invalid number.")
                
    for i in range(0, n):
        print("Number " + str(i + 1) + ": " + display_fraction(numbers[i]))
        
        
# Set up for output
counter = 1
# List to keep track of data. [0] is count, [1] is equation, [2] is sum, [3] is equation in fraction form
output = []

# First loop generates all combinations of subsets of certain length
for r in range(1, n + 1):
    subsets = combinations(numbers, r)
    # Second loop iterates through each of those subsets
    for subset in subsets:
        equation = ""
        equationFraction = ""
        total = 0.0
        # Third loop adds the numbers and saves the result
        for i in range(0, r):
            if i == 0:
                equation = equation + str(subset[i])
                equationFraction = equationFraction + display_fraction(subset[i])
            else:
                equation = equation + " + " + str(subset[i])
                equationFraction = equationFraction + " + " + display_fraction(subset[i])
            total = total + subset[i]
        output.append(("Sum #%s: " % str(counter), equation, total, equationFraction))
        print("%s%s = %s" % (output[counter - 1][0], output[counter - 1][1], output[counter - 1][2]))
        counter += 1

# Write results to files
print("Now creating files for output")
f = open('output_unsorted.txt', 'w')
for i in range(0, counter - 1):
    f.write("%s %s = %s\n" % (output[i][0], output[i][3], output[i][2]))
f.close()

output_sorted = sorted(output, key = lambda x: float(x[2]))
f2 = open('output_sums.txt', 'w')
f3 = open('output_sorted.txt', 'w')
for i in range(0, counter - 1):
    f2.write("%s %s\n" % (output_sorted[i][0], output_sorted[i][2]))
    f3.write("%s %s = %s\n" % (output_sorted[i][0], output_sorted[i][3], output_sorted[i][2]))
f2.close()
f3.close()

input("Finished. Press Enter to end...")