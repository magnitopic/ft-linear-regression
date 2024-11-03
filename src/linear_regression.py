import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

LEARNING_RATE = 0.01
NUM_ITERATIONS = 1000


def normalize(X):
    return (X - np.mean(X)) / np.std(X)


def denormalize_theta(X, Y, theta0_norm, theta1_norm):
    theta1 = theta1_norm * (np.std(Y) / np.std(X))
    theta0 = np.mean(Y) - theta1 * np.mean(X) + theta0_norm * np.std(Y)
    return theta0, theta1


def linear_regression(X_norm, Y_norm):
    theta0_norm = 0
    theta1_norm = 0

    for _ in range(NUM_ITERATIONS):
        # current prediction
        Y_pred_norm = theta1_norm * X_norm + theta0_norm

        # gradients
        m = len(X_norm)  # number of points
        D_theta0_norm = (1/m) * np.sum(Y_pred_norm - Y_norm)
        D_theta1_norm = (1/m) * np.sum(X_norm * (Y_pred_norm - Y_norm))

        # update parameters
        theta1_norm -= LEARNING_RATE * D_theta1_norm
        theta0_norm -= LEARNING_RATE * D_theta0_norm

    return theta0_norm, theta1_norm


def train(data):
    X = data['km'].values
    Y = data['price'].values
    X_norm = normalize(X)
    Y_norm = normalize(Y)
    theta0_norm, theta1_norm = linear_regression(X_norm, Y_norm)
    theta0, theta1 = denormalize_theta(X, Y, theta0_norm, theta1_norm)
    return theta0, theta1
