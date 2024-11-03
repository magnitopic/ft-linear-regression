# ft-linear-regression

Your first implementation of a machine learning algorithm.


<div align="center">
<img width="512" alt="Screenshot 2024-11-03 at 10 10 38" src="https://github.com/user-attachments/assets/b6e46a98-1b76-4de9-86db-ed1210a772e7">
</div>

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

## Clone and run project

```
git clone https://github.com/magnitopic/ft-linear-regression.git

cd ft-linear-regression

pip install -r requirements.txt

python src/main.py
```

## Math

$$ y = \theta_0 + \theta_1 \cdot x$$

$$ERROR = \frac{1}{m} \sum_{i=1}^{m} (\widehat{y}-y)^2$$

Cost function to minimize:

$$J = \frac{1}{2m} \sum_{i=1}^{m} (\widehat{y}-y)^2$$

$$J = \frac{1}{2m} \sum_{i=1}^{m} (\widehat{y}-(\theta_0 + \theta_1 \cdot x))^2$$

To minimize the cost, we need the partial derivative of the cost function.

> The gradient is: $\nabla J = \left( \frac{\partial J}{\partial \theta_0} , \frac{\partial J}{\partial \theta_1} \right) $

$$\frac{\partial J}{\partial \theta_0} = \frac{-1}{m} \sum_{i=1}^{m} (\widehat{y}-y)$$

$$\frac{\partial J}{\partial \theta_1} = \frac{-1}{m} \sum_{i=1}^{m} (\widehat{y}-y) \cdot x$$

$$ \theta_0 := \alpha \cdot \left( \frac{\partial J}{\partial \theta_0} \right) = \alpha \left( \frac{-1}{m} \sum(\widehat{y} - y) \right) $$

$$ \theta_1 := \alpha \cdot \left( \frac{\partial J}{\partial \theta_1} \right) = \alpha \left( \frac{-1}{m} \sum x\cdot(\widehat{y} - y) \right) $$

## Evaluation of the Model: Coefficient of Determination ($R^2$)

$R^2$ is a metric that varies between 0 and 1, where:

-   $R^2 = 0$: There is no linear relationship between the variables
-   $R^2 = 1$: There is a perfect linear relationship between the variables (all points are on the line)
-   $R^2 \approx 0.8$: Good fit in many contexts
-   $R^2 < 0.2$: Poor fit, suggests non-linear relationship or no relationship at all

$$R^2 = 1 - \dfrac{\sum_{i=1}^{n} (Y_i - \widehat{Y}_i)^2}{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}$$

## Correlation vs Causation

It's important in this statistics example to remember that:

-   Correlation does not imply causation
-   There may exist false correlations
    > [As shown by this website](https://www.tylervigen.com/spurious-correlations)
-   The value of $R^2$ should be interpreted with the specific context in mind
    -   In social sciences, a value of $R^2$ of 0.7 is considered high
    -   In physics, a value of $R^2$ of 0.7 is considered low
