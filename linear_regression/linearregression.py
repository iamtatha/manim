import numpy as np
# import matplotlib.pyplot as plt

def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    errors = predictions - y
    cost = (1 / (2 * m)) * np.sum(errors ** 2)
    return cost



def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    cost_history = []
    thetas = []

    for it in range(num_iters):
        thetas.append(theta.copy())
        predictions = X.dot(theta)
        errors = predictions - y
        cost_history.append(compute_cost(X, y, theta))
        # print('Iteration:', it, ' Cost:', cost_history[-1], ' Theta:', theta)

        theta -= (alpha / m) * X.T.dot(errors)

    return theta, cost_history, thetas



def lr():
    x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    noisy_y_values = [2.8, 5.3, 6.5, 9.1, 10.8, 13.7, 15.2, 16.5, 18.7]

    X = np.array([[1, x] for x in x_values])
    y = np.array(noisy_y_values).reshape(-1, 1)

    theta = np.random.rand(2, 1)*4 -2
    alpha = 0.01
    num_iters = 50

    theta_optimized, cost_history, thetas = gradient_descent(X, y, theta, alpha, num_iters)

    # plt.plot(cost_history)
    # plt.show()

    print("Optimized Theta:")
    # print(theta_optimized[1][0])
    # print("Final Cost:", cost_history[-1])

    return theta_optimized, cost_history, thetas


lr()