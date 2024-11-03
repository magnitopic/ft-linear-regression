import os
import predict
import pandas as pd
import aux.colors as c
import linear_regression
import matplotlib.pyplot as plt


def askForData():
    print(f"{c.BLUE}>> Please enter the route to the CSV file you wish to use for your {c.BOLD}dataset.{c.RESET}")
    print(f"{c.GRAY}(./data/data.csv)")
    path = input(f"{c.CYAN}--> {c.RESET}")
    if not path:
        path = "./data/data.csv"
    os.system('clear')
    return path


def readData(path):
    try:
        data = pd.read_csv(path)
        return data
    except:
        print(f"{c.RED}Error: Could not read data file.{c.RESET}")
        return None


def showDataGraph(data):
    plt.figure(figsize=(4, 3))
    plt.scatter(data['km'], data['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price of cars based on their mileage')
    plt.grid(color='green', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.tight_layout()
    plt.show()
    os.system('clear')


def showPredictionLineGraph(data, theta0, theta1):
    plt.figure(figsize=(4, 3))
    plt.scatter(data['km'], data['price'])
    plt.plot(data['km'], theta0 + theta1 * data['km'], color='red')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price of cars based on their mileage')
    plt.grid(color='green', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.tight_layout()
    plt.show()
    os.system('clear')


def showMenu():
    choice = None
    while True:
        print(f"\n{c.PURPLE}" + "="*21, "M E N U", "="*21)
        print(f"{c.BLUE}>> Please select an option from the following list:")
        print(f"{c.CYAN}1{c.BLUE} - Predict price")
        print(f"{c.CYAN}2{c.BLUE} - Train model")
        print(f"{c.YELLOW}\t--  BONUS  --")
        print(f"{c.CYAN}3{c.BLUE} - Show data points")
        print(f"{c.CYAN}4{c.BLUE} - Show prediction line")
        print(f"{c.CYAN}5{c.BLUE} - Show R² value")
        print(f"\n{c.CYAN}6{c.BLUE} - Exit{c.RESET}")
        choice = input(f"{c.CYAN}--> {c.RESET}")
        os.system('clear')
        try:
            choice = int(choice)
        except:
            print(f"{c.RED}Invalid input. Please try again.{c.RESET}")
            choice = None
            continue
        if choice not in range(1, 7):
            print(f"{c.RED}Value out of range. Please try again.{c.RESET}")
            choice = None
        else:
            break
    return choice


if __name__ == "__main__":
    theta0 = 0
    theta1 = 0

    print(f"{c.PURPLE}\nft-linear-regression{c.RESET} - {c.YELLOW}alaparic\n")
    path = askForData()
    data = readData(path)
    if data is None:
        exit()
    while True:
        choice = showMenu()
        if choice == 1:
            predict.prediction(theta0, theta1)
        elif choice == 2:
            theta0, theta1 = linear_regression.train(data)
            print(f"{c.GREEN}>> Model trained successfully!{c.RESET}")
            print(f"{c.BLUE}Theta0: {c.YELLOW}{theta0:.2f}{c.RESET}")
            print(f"{c.BLUE}Theta1: {c.YELLOW}{theta1:.2f}{c.RESET}")
        elif choice == 3:
            showDataGraph(data)
        elif choice == 4:
            showPredictionLineGraph(data, theta0, theta1)
        elif choice == 5:
            r_2 = linear_regression.determine_r2()
        elif choice == 6:
            print(f"{c.PURPLE}Bye! 👋{c.RESET}")
            exit()
