
def interpolate_lagrange(data: list):
    poly_size = len(data)
    denominator = [1 for i in range(poly_size)]
    for i in range(poly_size):
        for j in range(poly_size):
            denominator[i] *= data[i][0] - data[j][0] if not i == j else 1

    def fn(x):
        output = 0
        for i in range(poly_size):
            numerator = 1
            for j in range(poly_size):
                numerator *= x - data[j][0] if not i == j else 1
            output += data[i][1] * (numerator) / denominator[i]
        return output
    return fn