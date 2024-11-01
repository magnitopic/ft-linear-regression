# ft-linear-regression

Your first implementation of a machine learning algorithm.

## Description

This project is about implementing a simple linear regression algorithm. The goal is to predict the price of a car based on its mileage.

To do this we will use the following formula:

$$ y = \theta_0 + \theta_1 \cdot x$$

Where:

-   $y$ is the price of the car (dependent variable)
-   $x$ is the mileage of the car (independent variable)
-   $\theta_0$ is the intercept
-   $\theta_1$ is the slope

To figure out the values of $\theta_0$ and $\theta_1$ we will use the [gradient descent algorithm](https://en.wikipedia.org/wiki/Gradient_descent).

## Math

$$ERROR = \frac{1}{m} \sum_{i=1}^{m} (\widehat{y}-y)^2$$

$$ y = \theta_0 + \theta_1 \cdot x$$

Cost function to minimize:

$$J = \frac{1}{2m} \sum_{i=1}^{m} (\widehat{y}-y)^2$$

$$J = \frac{1}{2m} \sum_{i=1}^{m} (\widehat{y}-(\theta_0 + \theta_1 \cdot x))^2$$

To minimize the cost, we need the partial derivative of the cost function.

> The gradient is: $$\nabla J = \left( \frac{\partial J}{\partial \theta_0} , \frac{\partial J}{\partial \theta_0} \right) $$

$$\frac{\partial J}{\partial \theta_0} = \frac{-1}{m} \sum_{i=1}^{m} (\widehat{y}-y)$$

$$\frac{\partial J}{\partial \theta_1} = \frac{-1}{m} \sum_{i=1}^{m} (\widehat{y}-y) \cdot x$$

$$ \theta_0 := \alpha \cdot \left( \frac{\partial J}{\partial \theta_0} \right) = \alpha \left( \frac{-1}{m} \sum(\widehat{y} - y) \right) $$

$$ \theta_1 := \alpha \cdot \left( \frac{\partial J}{\partial \theta_1} \right) = \alpha \left( \frac{-1}{m} \sum x(\widehat{y} - y) \right) $$
