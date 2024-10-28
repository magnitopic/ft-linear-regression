import json

# load json file with theta values
try:
    with open('src/theta.json') as file:
        data = json.load(file)

    theta0 = float(data["theta0"])
    theta1 = float(data["theta1"])
except:
    print("\033[2;30mNotice: Could not read file. Reverting to default values.\033[0m")
    theta0 = 0
    theta1 = 0


def estimatePrice(mileage:int):
    estimatedPrice = theta0 + (theta1 * mileage)
    return estimatedPrice


if __name__ == '__main__':
    print(estimatePrice(2000))
