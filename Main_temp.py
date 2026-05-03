# from Temperature import CtoF
# from Temperature import FtoC
# from Temperature import Cto
from Temperature import CtoF
from Temperature import FtoC
from Temperature import CtoK

def main():
    while True:
        print("₹1. Celcius to Kelvin")
        print("2. Celcius to Fahrenheit")
        print("3. Fahrenheit to Celcius")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            celcius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Kelvin: ", CtoF.convert(celcius))
        elif choice == 2:
            celcius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Fahrenheit: ", FtoC.convert(celcius))
        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celcius: ", CtoK.convert(fahrenheit))
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
