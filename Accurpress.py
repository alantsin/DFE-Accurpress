from fractions import Fraction
from past.types import basestring

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
    n = 11
    numbers = [0.75, 1, 1.25, 2.25, 4, 5.25, 8.5, 12, 17, 48, 56]
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
# List to keep track of data. [0] is count, [1] is equation, [2] is sum
output = []

# Summation loops
# First loop to keep track of total numbers to sum
for numbersToAdd in range(1, n + 1):
    # Second loop to keep track of the start index
    for startIndex in range(0, n):
        # If only one number, the sum is that number
        if numbersToAdd == 1:
            output.append(("Sum #%s:" % str(counter), display_fraction(numbers[startIndex]), numbers[startIndex]))
            print("%s %s = %s" % (output[counter - 1][0], output[counter - 1][1], display_fraction(output[counter - 1][2])))
            counter += 1
        # Conditional to determine if this combination i and j would exceed the number of numbers
        elif numbersToAdd + startIndex > n:
            #print("Combination of numbersToAdd and startIndex exceed the maximum index")
            break
        # Else, add the numbers and store it
        else:
            tempSum = 0.0
            tempSumString = ""
            total = 0.0
            # Third loop adds the numbers
            for currentIndex in range(startIndex, numbersToAdd + startIndex):
                # If the current index is less than the final number, store in a temporary sum
                if currentIndex < numbersToAdd + startIndex - 1:   
                    if currentIndex == startIndex:
                        tempSumString = tempSumString + display_fraction(numbers[currentIndex])
                    else:
                        tempSumString = tempSumString + " + " + display_fraction(numbers[currentIndex])  
                    tempSum += numbers[currentIndex]

                    # print("Temp sum: " + str(tempSum))
                # Otherwise, add tempSum to the final number and store it
                else:
                    for endIndex in range(currentIndex, n):
                        tempSumStringFinal = tempSumString + " + " + display_fraction(numbers[endIndex])
                        total = tempSum + numbers[endIndex]
                        output.append(("Sum #%s: " % str(counter), tempSumStringFinal, total))
                        print("%s %s = %s" % (output[counter - 1][0], output[counter - 1][1], display_fraction(output[counter - 1][2])))
                        counter += 1
                
# Write results to files
print("Now creating files for output")
f = open('output_unsorted.txt', 'w')
for i in range(0, counter - 1):
    f.write("%s %s = %s\n" % (output[i][0], output[i][1], display_fraction(output[i][2])))
f.close()

output_sorted = sorted(output, key = lambda x: float(x[2]))
f2 = open('output_sums.txt', 'w')
f3 = open('output_sorted.txt', 'w')
for i in range(0, counter - 1):
    f2.write("%s %s\n" % (output_sorted[i][0], display_fraction(output_sorted[i][2])))
    f3.write("%s %s = %s\n" % (output_sorted[i][0], output_sorted[i][1], display_fraction(output_sorted[i][2])))
f2.close()
f3.close()

# Final line to prevent from closing
input("Files created. Press Enter to finish.")
    