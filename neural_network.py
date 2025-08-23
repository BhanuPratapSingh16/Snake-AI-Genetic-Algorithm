import numpy as np

input_units = 24
hidden_units_1 = 18
hidden_units_2 = 18
output_units = 3

def get_weights(individual):
    W1 = individual[0:hidden_units_1 * input_units]
    W2 = individual[hidden_units_1 * input_units : hidden_units_1 * input_units + hidden_units_2 * hidden_units_1]
    W3 = individual[hidden_units_1 * input_units + hidden_units_2 * hidden_units_1:]
    return W1.reshape(hidden_units_1, input_units), W2.reshape(hidden_units_2, hidden_units_1), W3.reshape(output_units, hidden_units_2)

def softmax(Z):
    return np.exp(Z.T) / np.sum(np.exp(Z.T), axis=0)


def forward_propagation(X, individual):
    W1, W2, W3 = get_weights(individual)
    Z1 = np.matmul(W1, X.T)
    A1 = np.tanh(Z1)
    Z2 = np.matmul(W2, A1.T)
    A2 = np.tanh(Z2)
    Z3 = np.matmul(W3, A2.T)
    A3 = softmax(Z3)
    return A3
