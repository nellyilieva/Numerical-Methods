def divided_difference(nodes, values):
    """Recursive function for finding the divided difference"""
    n = nodes.size
    if n == 1:
        return values[0]
    return ((divided_difference(nodes[1:n], values[1:n]) - divided_difference(nodes[0:n-1], values[0:n-1]))
            / (nodes[n-1] - nodes[0]))


def newton_poly(nodes, values, x):
    """It calculates the Newton polynom in point x"""
    n = nodes.size
    polynom = 0.0
    product = 1.0
    for i in range(n):
        polynom += divided_difference(nodes[0:i + 1], values[0:i + 1]) * product
        product *= (x - nodes[i])
    return polynom
