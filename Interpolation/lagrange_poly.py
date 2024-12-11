def lagrange_poly(f, nodes, x):
    """It calculates the approximate value of Lagrange polynom"""

    n = len(nodes)
    result = 0.0

    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x - nodes[j]) / (nodes[i] - nodes[j])

        result += f(nodes[i]) * L_i

    return result


def lagrange_poly(x_nodes, y_nodes, x):
    n = x_nodes.size
    result = 0.0

    for i in range(n):
        l_i = y_nodes[i]
        for j in range(n):
            if i != j:
                l_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += l_i
    return result