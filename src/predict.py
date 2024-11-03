import json
import aux.colors as c


def estimatePrice(mileage: int, theta0: float, theta1: float):
    estimatedPrice = theta0 + (theta1 * mileage)
    return estimatedPrice


def prediction(theta0, theta1):
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

    price = round(estimatePrice(milage, theta0, theta1), 2)
    print("_"*20)
    print(f"{c.GREEN}y = {theta0:.2f} + {theta1:.2f} * x{c.RESET}")
    print("_"*20)
    print(f"{c.BLUE}For the milage you entered:\n{c.YELLOW}{milage} KM\n{c.BLUE}The estimated price is:\n{c.YELLOW}{price:.2f} €{c.RESET}")
