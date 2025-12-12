def add(result, counter):
    if counter == 0:
        print("Pick 2 numbers to add.")
        num1 = input("First numer: ")
        num2 = input("Second number: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            new_result = num1 + num2
            return new_result
        except ValueError:
            print("Invalid Number")
            return None
    else:
        num_input = input(f"Pick a number to add to {result}: ")
        try:
            num = float(num_input)
            new_result = result + num
            return new_result
        except ValueError:
            print("Invalid number.")
            return None

def Subtract(result, counter):
    if counter == 0:
        print("Pick 2 numbers to subtract.")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            new_result = num1 - num2
            return new_result
        except ValueError:
            print("Invalid number.")
            return None
    else:
        num_input = input(f"Pick a number to subtract from {result}: ")
        try:
            num = float(num_input)
            new_result = result - num
            return new_result
        except ValueError:
            print("Invalid number.")
            return None

def Multiply(result, counter):
    if counter == 0:
        print("Pick 2 numbers to multiply.")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            new_result = num1 * num2
            return new_result
        except ValueError:
            print("Invalid number.")
            return None
    else:

        num_input = input(f"Pick a number to multiply {result} with: ")
        try:
            num = float(num_input)
            new_result = result * num
            return new_result
        except ValueError:
            print("Invalid number.")
            return None


def Divide(result, counter):
    if counter == 0:
        print("Pick 2 numbers to divide.")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            if num2 == 0:
                print("Cannot divide with 0.")
                return result
            new_result = num1 / num2
            return new_result
        except ValueError:
            print("Invalid number.")
            return None
    else:
        num_input = input(f"Pick a number to divide {result} with: ")
        try:
            num = float(num_input)
            if num == 0:
                print("Cannot divide with 0.")
                return None
            new_result = result / num
            return new_result
        except ValueError:
            print("Invalid number.")
            return None

result = 0

choices = ["1", "2", "3", "4", "5"]

choice = None

counter = 0

while choice != '5':

    choice = input("1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit")

    if choice not in choices:

        print ("Wrong input")
        continue

    elif choice == '1':

        new_result = add(result, counter)
    
    elif choice == '2':

        new_result = Subtract(result, counter)

    elif choice == '3':

        new_result = Multiply(result, counter)

    elif choice == '4':

        new_result = Divide(result, counter)

    if new_result is None:
        print("Operation failed please try again.")
        continue

    result = new_result
    counter += 1
    print(f"The current result is: {result}")
