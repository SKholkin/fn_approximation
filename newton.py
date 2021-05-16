
def devided_diff(data_points):
    if len(data_points) == 1:
        return data_points[0][1]
    return (devided_diff(data_points[1:]) - devided_diff(data_points[:-1])) / (data_points[-1][0] - data_points[0][0])

def interpolate_newton(data: list):
    devided_diffs = []
    for i in range(len(data)):
        devided_diffs.append(devided_diff(data[:(i + 1)]))
    def fn(x):
        result = 0
        for i in range(len(data)):
            part = 1
            for j in range(len(data) - 1):
                part *= (x - data[j][0])
            result += part * devided_diffs[i]
        return result
    return fn

