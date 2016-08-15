#Exercise 1
nameFile = open("name.txt", "w")
nameIn = input("Please input your name: ")
print(nameIn, file=nameFile)
nameFile.close()

#Exercise 2
nameFile = open("name.txt", "r")
nameOut = nameFile.read().strip()
print("Your name is: ", nameOut)

#Exercise 3
numbersFile = open("numbers.txt", "r")
num1 = int(numbersFile.readline())
num2 = int(numbersFile.readline())
print ("The total is: ", num1 + num2)
numbersFile.close()