def length_converter(value, from_unit, to_unit):
    if from_unit == 'meters':
        if to_unit == 'feet':
            return (value * 3.281)
        elif to_unit == 'inches':
            return (value * 39.37)
        elif to_unit =='meters':
            return value
        else:
            raise ValueError("Invalid input for length conversion.")
    elif from_unit == 'feet':
        if to_unit == 'meters':
            return (value / 3.281)
        elif to_unit == 'inches':
            return (value * 12)
        elif to_unit =='feet':
            return value
        else:
            raise ValueError("Invalid input for length conversion.")
    elif from_unit == 'inches':
        if to_unit == 'meters':
            return (value / 39.37)
        elif to_unit == 'feet':
            return (value / 12)
        elif to_unit =='inches':
            return value
        else:
            raise ValueError("Invalid input for length conversion.")
    else:
        raise ValueError("Invalid input for length conversion.")

def mass_converter(value, from_unit, to_unit):
    if from_unit == 'kilograms':
        if to_unit == 'pounds':
            return (value * 2.205)
        elif to_unit == 'ounces':
            return (value * 35.274)
        elif to_unit =='kilograms':
            return value
        else:
            raise ValueError("Invalid input for mass conversion.")
    elif from_unit == 'pounds':
        if to_unit == 'kilograms':
            return (value / 2.205)
        elif to_unit == 'ounces':
            return (value * 16)
        elif to_unit =='pounds':
            return value
        else:
            raise ValueError("Invalid input for mass conversion.")
    elif from_unit == 'ounces':
        if to_unit == 'kilograms':
            return (value / 35.274)
        elif to_unit == 'pounds':
            return (value / 16)
        elif to_unit =='ounces':
            return value
        else:
            raise ValueError("Invalid input for mass conversion.")
    else:
            raise ValueError("Invalid input for mass conversion.")

def temperature_converter(value, from_unit, to_unit):    
    if from_unit == 'celcius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'celcius':
            return value
        else:
            raise ValueError("Invalid input for temperature conversion.")
    elif from_unit == 'fahrenheit':
        if to_unit == 'celcius':
            return (value - 32) * 5/9
        elif to_unit == 'fahrenheit':
            return value
        else:
            raise ValueError("Invalid input for temperature conversion.")
    else:
        raise ValueError("Invalid input for temperature conversion.")

def currency_converter(value, from_unit, to_unit):                         #Currency exchange rates obtained from GoogleFinance on 02/21/2024
    if from_unit == 'USD':
        if to_unit == 'GBP':
            return (value *.79)
        elif to_unit == 'EUR':
            return (value * .93)
        elif to_unit =='USD':
            return value
        else:
            raise ValueError("Invalid input for currency conversion.")
    elif from_unit == 'GBP':
        if to_unit =='USD':
            return (value * 1.26)
        elif to_unit == 'EUR':
            return (value * 1.17)
        elif to_unit =='GBP':
            return value
        else:
            raise ValueError("Invalid input for currency conversion.")
    elif from_unit == 'EUR':
        if to_unit =='USD':
            return (value * 1.08)
        elif to_unit == 'GBP':
            return (value * .86)
        elif to_unit =='EUR':
            return value
        else:
            raise ValueError("Invalid input for currency conversion.")
    else:
            raise ValueError("Invalid input for currency conversion.")


def main():
    print("Welcome to the Unit Converter Application")
    while True:
        print("Choose a number from the menu for the conversion type you wish to process, or enter 5 to exit the program:")
        print("1. Length")
        print("2. Mass")
        print("3. Temperature")
        print("4. Currency")
        print("5. Exit")

        choice = input("Please enter your number choice: ")
        if choice == "1":
            print("You selected Length Conversion.")
            while True:
                try:
                    value = input("Please enter the number value you wish to convert: ")
                    value = int(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for conversion.")
            from_unit = input("Please enter the current unit of measurement (meters, feet, inches): ")
            to_unit = input("Please enter the unit of measurement you wish to convert the value to (meters, feet, inches): ")
            result = round(length_converter(value, from_unit, to_unit), 2)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif choice == "2":
            print("You selected Mass Conversion.")
            while True:
                try:
                    value = input("Please enter the number value you wish to convert: ")
                    value = int(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for conversion.")
            from_unit = input("Please enter the current unit of measurement (kilograms, pounds, ounces): ")
            to_unit = input("Please enter the unit of measurement you wish to convert the value to (kilograms, pounds, ounces): ")
            result = round(mass_converter(value, from_unit, to_unit), 2)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif choice == "3":
            print("You selected Temperature Conversion.")
            while True:
                try:
                    value = input("Please enter the number value you wish to convert: ")
                    value = int(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for conversion.")
            from_unit = input("Please enter the current unit of measurement (celcius, fahrenheit): ")
            to_unit = input("Please enter the unit of measurement you wish to convert the value to (celcius, fahrenheit): ")
            result = round(temperature_converter(value, from_unit, to_unit), 2)
            print(f"{value} degrees {from_unit} is equal to {result} degrees {to_unit}.")

        elif choice == '4':
            print("You selected Currency Conversion.")
            while True:
                try:
                    value = input("Please enter the number value you wish to convert: ")
                    value = int(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for conversion.")
            from_unit = input("Please enter the current unit of currency (USD, GBP, EUR): ")
            to_unit = input("Please enter the unit of currency you wish to convert the value to (USD, GBP, EUR): ")
            result = round(currency_converter(value, from_unit, to_unit), 2)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif choice == "5":
            print("Thank you for using the Unit Converter Application. Goodbye!")
            break
        else:
            print("Invalid choice, Please select from the available number options and try again.")

if __name__ == "__main__":
    main()