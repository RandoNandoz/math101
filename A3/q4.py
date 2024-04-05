from math import sin, pi
import pandas as pd
import numpy as np

values = pd.read_csv(r"./A17.csv", names=[r"f"])

n = values.iloc[-1].name

dx = pi/n

x_axis = np.arange(0, np.pi + dx, dx)

values['x'] = x_axis


def tr_rule(f: pd.Series, x: pd.Series, dx: float, R: int):
    return (
        (2 / pi) * dx * (
            (1/2 * f.iloc[0] * sin(R * x.iloc[0])) +
            sum(f.iloc[1:-1] * (x.iloc[1:-1] * R).map(sin)) +
            (1/2 * f.iloc[-1] * sin(R * x.iloc[-1]))
        )
    )


b_k_raw: list[float] = []

last_result = float('inf')
i = 1
while round(last_result, 6) > 0:
    last_result = tr_rule(values['f'], values['x'], dx, i)
    b_k_raw.append(last_result)
    i += 1

b_k = list(filter(lambda x: x != 0, [round(b_i) for b_i in b_k_raw]))

print(b_k)

resulting_chars = [chr(b_i) for b_i in b_k]

print("".join(resulting_chars))
