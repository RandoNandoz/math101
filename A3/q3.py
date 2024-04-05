from math import pi, sin

R = pi / 2


def tr_rule(values: list[float], dx: float, n: int) -> float:
    assert len(values) == 9
    x_k = [dx * i for i in range(9)]
    return (1 / R) * (
        dx * (
            1/2 * values[0] * sin(n * x_k[0]) +
            sum([values[i] * sin(n * x_k[i]) for i in range(1, 8)]) +
            1/2 * values[8] * sin(n * x_k[8])
        )
    )


f_k: list[float] = [0.0, 409.3, 149.8, -53.9, 75.0, 19.3, -52.2, 50.5, 0.0]

for i in range(1, 6):
    print(f"B_{i}(f) = {round(tr_rule(f_k, pi / 8, i), 3)}")
