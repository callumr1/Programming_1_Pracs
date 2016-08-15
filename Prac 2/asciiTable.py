
lower = 10
upper = 100


#print("Enter a number: {}-{} ".format(lower, upper))

#for i in range (10, 120, 11):
    #print("{} {}" .format(i, chr(i)))


def get_number(lower, upper):
    num_valid = False

    while not num_valid:

        num = int(input("Enter a number: "))
        if num < lower:
            print ("Error, the number you input is less than {}".format(lower))
        elif num > upper:
            print("Error, the number you input is greater than {}".format(upper))
        else:
            print("Thankyou, your number ({}) is valid!".format(num))
            num_valid = True

get_number(lower, upper)