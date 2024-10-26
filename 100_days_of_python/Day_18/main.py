from Day_18.calculatorclass import CalculatorClass

def main():
    calculator = CalculatorClass()

    while True:
        print("Kindly Select the following options")
        print("1. Addition")
        print("2. Substration")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter the choice (1/2/3/4)"))

        if choice in (1,2,3,4):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid Value")
                continue

            if choice == 1:
                print(calculator.add(num1,num2))
            elif choice == 2:
                print(calculator.sub(num1,num2))
            elif choice == 3:
                print(calculator.mul(num1,num2))
            elif choice == 4:
                print(calculator.div(num1,num2))

            next_calculation = input("Do you want to perfrom the next Calculation? (yes/no)")
            if next_calculation.lower() != "yes":
                break

        else:
            print("Invalid Input")

main()




