def main():
    numbers = []
    print("Please input 5 numbers")

    for count in range(1, 6):
        num = int(input("Enter number {}: ".format(count)))
        numbers.append(num)

    average = calc_average(numbers)
    print_numbers(numbers, average)

def calc_average(numbers):
    average = sum(numbers) / len(numbers)
    return average

def print_numbers(numbers, average):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the number is {}".format(average))

main()