import json
import aux.colors as c

# load json file with theta values
try:
    with open('src/theta.json') as file:
        data = json.load(file)

    theta0 = float(data["theta0"])
    theta1 = float(data["theta1"])
except:
    print(f"{c.GRAY}Notice: Could not read json file. Reverting to default values.{c.RESET}")
    theta0 = 0
    theta1 = 0


def estimatePrice(mileage:int):
    estimatedPrice = theta0 + (theta1 * mileage)
    return estimatedPrice


def prediction():
    milage = None

    # input user for milage value
    while milage == None:
        try:
            milage = int(input(f"{c.BLUE}Please enter the milage of the car: {c.RESET}"))
            if milage < 0:
                milage = None
                raise Exception("")
        except:
            print(f"{c.RED}Invalid input. Please try again{c.RESET}")

    price = round(estimatePrice(milage), 2)
    print("_"*20)
    print(f"{c.GREEN}y = {theta0:.2f} + {theta1:.2f} * x{c.RESET}")
    print("_"*20)
    print(f"{c.BLUE}For the milage you entered:\n{c.YELLOW}{milage} KM\n{c.BLUE}The estimated price is:\n{c.YELLOW}{price:.2f} €{c.RESET}")
 