from argparse import ArgumentParser
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

from lagrange import interpolate_lagrange
from newton import interpolate_newton
from learned_poly import interpolate_learned_poly


def interpolate(build_fn, data: list, verbose=True):
    eps = 1e-6
    interpolate_fn = build_fn(data)
    start = min(data, key=lambda x: x[0])[0] + eps
    stop = max(data, key=lambda x: x[0])[0] - eps
    if verbose:
        plt.plot(np.arange(start, stop, 0.01), [interpolate_fn(x) for x in np.arange(start, stop, 0.01)])
        plt.ylim([-2, 2])
        plt.show()


def data_parse(path: str):
    data = pd.read_csv(path)
    output = []
    for i in data.iloc():
        output.append((float(i.x), float(i.y)))
    return output


def scipy_interpolation_fn_shell(kind='linear'):
    def build_fn(data: list):
        x = [item[0] for item in data]
        y = [item[1] for item in data]
        return interp1d(x, y, kind=kind)
    return build_fn


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--method', type=str, default='lagrange',
     choices=['lagrange', 'newton', 'learned_poly', 'scipy_linear', 'scipy_cubic'],
        help='Method used for interpolation')
    parser.add_argument('--data', type=str, default='data.csv', help='Path to data')
    args = parser.parse_args(args=sys.argv[1:])
    data = data_parse(args.data)
    if args.method == 'lagrange':
        build_fn = interpolate_lagrange
    elif args.method == 'newton':
        build_fn = interpolate_newton
    elif args.method == 'scipy_linear':
        build_fn = scipy_interpolation_fn_shell(kind='linear')
    elif args.method == 'scipy_cubic':
        build_fn = scipy_interpolation_fn_shell(kind='cubic')

    interpolate(build_fn, data)
