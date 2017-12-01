from fractions import Fraction

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
        print(Fraction(num))        
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
        print("Number " + str(i + 1) + ": " + str(numbers[i]))

        
# Set up for output
counter = 1
# Output 1: Equations with unsorted sums
output_unsorted = []
# Output 2: Sorted sums only
output_sums = []
# Output 3: Equations and sorted sums
output_sorted = []

# Summation loops
# First loop to keep track of total numbers to sum
for numbersToAdd in range(1, n + 1):
    # Second loop to keep track of the start index
    for startIndex in range(0, n):
        # If only one number, the sum is that number
        if numbersToAdd == 1:
            print("Sum #" + str(counter) + ": " + str(numbers[startIndex]))
            counter += 1
        # Conditional to determine if this combination i and j would exceed the number of numbers
        elif numbersToAdd + startIndex > n:
            print("Combination of numbersToAdd and startIndex exceed the maximum index")
            break
        # Else, add the numbers and store it
        else:
            tempSum = 0.0
            sum = 0.0
            # Third loop adds the numbers
            for currentIndex in range(startIndex, numbersToAdd + startIndex):
                # If the current index is less than the final number, store in a temporary sum
                if currentIndex < numbersToAdd + startIndex - 1:
                    tempSum += numbers[currentIndex]
                    # print("Temp sum: " + str(tempSum))
                # Otherwise, add tempSum to the final number and store it
                else:
                    for endIndex in range(currentIndex, n):
                        sum = tempSum + numbers[endIndex]
                        print("Sum #" + str(counter) + ": " + str(sum))
                        counter += 1
                

# Final line to prevent from closing
#input("Press Enter to finish")
    