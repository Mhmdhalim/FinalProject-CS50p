import sys, csv, cowsay, pyTextColor
from tabulate import tabulate

# from pyfiglet import figlet_format

# FILES USED IN THIS PROGRAMM
services = "services.csv"
fruits = "fruits.csv"
vegatables = "vegatables.csv"
Shirts = "Shirts.csv"
check = False


pytext = pyTextColor.pyTextColor()
text = "WELCOME!"
# text = figlet_format("WELCOME!")
text = pytext.format_text(text, color="magenta", bgcolor="black")
print()
print(text)
# GLOBAL CLIENT
name_of_customer = input("Write your name, Please.\n").strip()


def main():
    # Find out the service 1 number
    if not check:
        welcome_to_the_customer()
    num_of_services = return_services()
    if num_of_services == "1":
        calculator()
    elif num_of_services == "2":
        ideal_weight_for_height()
    elif num_of_services == "3":
        Shirt_market()
    elif num_of_services == "4":
        fruits_vegatables_market()


# Find out the service number
def welcome_to_the_customer():
    global check
    while True:
        check_ = (
            input(
                f"""hello Mr/s. {name_of_customer.title()}, Are you need service?\nPlease type Y for YES or N for NO. """
            )
            .strip()
            .lower()
        )
        if check_ == ("y" or "yes") or check_ == ("n" or "no"):
            break
    if check_ in ["y", "yes"]:
        check = True
    else:
        sys.exit(
            cowsay.daemon(
                """\nYou're welcome!. Please let me know if you have any other questions or
            need assistance finding anything else in the store. Enjoy the rest of your day!"""
            )
        )


# Check
def return_services():
    global check
    if check:
        with open(services, "r") as file:
            reader = csv.reader(file)
            print(
                f"Good morning Mr. {name_of_customer.title()}, Welcome to my website.\n"
                + "We are offfering....\n",
                tabulate(reader, headers=["num", "srevice"], tablefmt="pretty"),
            )
            # customer Q1
        while True:
            customer1_Q1 = input(
                "What do you want?\nPlease select the service number. "
            ).strip()
            """""
                1 calculator
                2 Calculate the ideal weight for height
                3 t-shirt market
                4 fruits and vegetable market
            """ ""
            if customer1_Q1 in ["1", "2", "3", "4"]:
                break
        return customer1_Q1


# recursion of all services
def other_service():
    service = input("Do you want another service? ")
    if service.upper() == "Y" or service.upper() == "YES":
        main()
    elif service.upper() == "N" or service.upper() == "NO":
        sys.exit(
            cowsay.daemon(
                """\nYou're welcome!. Please let me know if you have any other questions or
            need assistance finding anything else in the store. Enjoy the rest of your day!"""
            )
        )
    else:
        other_service()


# CALCUALTOR
def calculator():
    # input for NUMBERS
    print("Welcome to in the calculator.")
    i, numbers = 1, []
    # check type of input
    while True:
        num_of_numbers = input("How many numbers do you want to enter? ").strip()
        if len(num_of_numbers) != 0 and num_of_numbers.isdigit():
            break

    for _ in range(int(num_of_numbers)):
        n = int(input(f"Enter your {number_to_ordinal(i)} number: "))

        i += 1
        numbers.append(n)
    if len(numbers) == 1:
        print(numbers[0])
    else:
        while True:
            operation = input(
                """
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
Math operation: """
            )
            if operation in ["+", "-", "*", "/"]:
                break

        if operation == "+":
            print(sum(numbers))
            numbers = []
        elif operation == "-":
            numbers[0], total = -1 * numbers[0], 0
            for num in numbers:
                total -= num
            print(total)
            numbers = []
        elif operation == "*":
            total = 1
            for num in numbers:
                total *= num
            print(total)
            numbers = []
        elif operation == "/":
            total = numbers[0]
            try:
                for num in range(1, len(numbers)):
                    total /= numbers[num]
                print(total)
            except ZeroDivisionError:
                print()
                print("ERROR: DIVIDE BY ZERO")
            numbers = []

    again_calculator()


# RECURSION OF CALCULATOR
def again_calculator():
    calc_again = input(
        """
Do you want to calculate again?
Please type Y for YES or N for NO.
"""
    )

    if calc_again.upper() == "Y" or calc_again.upper() == "YES":
        calculator()
    elif calc_again.upper() == "N" or calc_again.upper() == "NO":
        other_service()
    else:
        again_calculator()


# CALCULATE THE IDEAL WEIGHT
def ideal_weight_for_height():
    print("Welcome, Please fill the following:")
    # check gender
    while True:
        gender = input("Gender: ").strip().lower()
        if gender == "male" or gender == "female":
            break

    # check Height
    while True:
        Height = input("Height: ").strip()
        if len(Height) != 0 and Height.isdigit():
            Height = int(Height)
            if Height < 3:
                Height *= 100
            break
    # check Age
    while True:
        Age = input("Age: ").strip()
        if len(Age) != 0 and Age.isdigit():
            Age = int(Age)
            break
    # MALE
    if gender == "male":
        Ideal_weight = 50 + 0.91 * (Height - 152.4) - (Age - 20) * 0.66
        print(f"{Ideal_weight:.2f} kg")
    # FEMALE
    elif gender == "female":
        Ideal_weight = 45.5 + 0.91 * (Height - 152.4) - (Age - 20) * 0.66
        print(f"{Ideal_weight:.2f} kg")

    again_ideal()


# RECURSION OF THE IDEAL WEIGHT OF HEIGHT
def again_ideal():
    calc_again = input(
        """
Do you want to calculate again?
Please type Y for YES or N for NO.
"""
    )

    if calc_again.upper() == "Y" or calc_again.upper() == "YES":
        ideal_weight_for_height()
    elif calc_again.upper() == "N" or calc_again.upper() == "NO":
        other_service()
    else:
        again_ideal()


a = True
# FRUITS AND VEGATABLES MARKET
def fruits_vegatables_market():
    global a
    if a:
        print("Welcome to in the market.")
        a = False
    total_fruits, total_vegatables, ch = 0, 0, ""
    while True:
        f_v = input("Are you need fruits or vegatables? ").strip().lower()
        if compare(f_v, "fruits") == True:
            ch = "f"
            break
        elif compare(f_v, "vegatables"):
            ch = "v"
            break

    if ch == "f":
        with open(fruits, "r") as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers=["Fruits", "Price"], tablefmt="pretty"))

        with open(fruits, "r") as file:
            reader = csv.reader(file)
            list_fruits = list(reader)
            i = 1
            while True:
                fr = input(f"Enter your {number_to_ordinal(i)} fruit: ").strip().title()
                for fruit in list_fruits:
                    if fr == fruit[0]:
                        total_fruits += float(fruit[1])
                        i += 1
                        break
                if len(fr) == 0 and total_fruits > 0:
                    print(f"Total price of fruits: ${total_fruits}")
                    break
    elif ch == "v":
        with open(vegatables, "r") as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers=["Fruit", "Price"], tablefmt="pretty"))

            with open(vegatables, "r") as file:
                reader = csv.reader(file)
                list_vegatables = list(reader)
                i = 1
                while True:
                    ve = (
                        input(f"Enter your {number_to_ordinal(i)} vegatable: ")
                        .strip()
                        .title()
                    )
                    for vegatable in list_vegatables:
                        if ve == vegatable[0]:
                            i += 1
                            total_vegatables += float(vegatable[1])
                            break
                    if len(ve) == 0 and total_vegatables:
                        print(f"Total price of vegatables: ${total_vegatables}")
                        break
    market_fruits_vegatables()


def compare(word1, word2):
    return word1 in word2 or word2 in word1


def market_fruits_vegatables():
    calc_again = input(
        """
Do you want anything else?
Please type Y for YES or N for NO.
"""
    )

    if calc_again.upper() == "Y" or calc_again.upper() == "YES":
        fruits_vegatables_market()
    elif calc_again.upper() == "N" or calc_again.upper() == "NO":
        other_service()
    else:
        market_fruits_vegatables()


# SHIRT MARKET
def Shirt_market():
    print("Welcome to in the market. We are offering...")
    total_shirts = 0

    with open(Shirts, "r") as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers=["Prices", "Shirts"], tablefmt="pretty"))

    print("Please type what do you need? ")
    with open(Shirts, "r") as file:
        reader = csv.reader(file)
        list_shirts = list(reader)
        i = 1
        while True:
            shirt = (
                input(f"Enter your {number_to_ordinal(i)} t-shirt: ").strip().title()
            )

            for shirts in list_shirts:
                if shirt == shirts[0].title():
                    i += 1
                    total_shirts += float(shirts[1])
                    break

            if len(shirt) == 0 and total_shirts > 0:
                print(f"Total price of fruits: ${total_shirts}")
                break
    Shirt_market__()


# recursion of t-shirt market
def Shirt_market__():
    calc_again = input(
        """
Do you want anything else?
Please type Y for YES or N for NO.
"""
    )

    if calc_again.upper() == "Y" or calc_again.upper() == "YES":
        Shirt_market()
    elif calc_again.upper() == "N" or calc_again.upper() == "NO":
        other_service()
    else:
        Shirt_market()


def number_to_ordinal(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the number ends with 1, 2, or 3 but not with 11, 12, or 13
    if number_str.endswith("1") and not number_str.endswith("11"):
        ordinal = number_str + "st"
    elif number_str.endswith("2") and not number_str.endswith("12"):
        ordinal = number_str + "nd"
    elif number_str.endswith("3") and not number_str.endswith("13"):
        ordinal = number_str + "rd"
    else:
        ordinal = number_str + "th"

    return ordinal


if __name__ == "__main__":
    main()
