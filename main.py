import numpy as np
import matplotlib.pyplot as plt


def fuzzy_number_m(x, m):
    return np.where(
        x >= m,
        1 / (1 + (x - m) ** 2),
        1 / (1 + (m - x) ** 2),
    )


def fuzzy_number_neg_m(x, m):
    return np.where(
        x >= m,
        1 / (1 + (x + m) ** 2),
        1 / (1 + (m + x) ** 2),
    )


def add_fuzzy_numbers(mu1, mu2):
    return np.minimum(mu1, mu2)


def main():
    try:
        m1 = float(input("Введіть значення m: "))
        m2 = float(input("Введіть значення -m: "))
    except ValueError:
        print("Введені значення мають бути числами!")
        exit()

    x = np.linspace(-max(m1, m2) - 10, max(m1, m2) + 10, 500)

    mu_m1 = fuzzy_number_m(x, m1)
    mu_m2 = fuzzy_number_neg_m(x, m2)
    mu_sum = add_fuzzy_numbers(mu_m1, mu_m2)

    plt.figure(figsize=(10, 6))
    plt.plot(x, mu_m1, label=f"Нечітке число m ({m1})", color="blue")
    plt.plot(x, mu_m2, label=f"Нечітке число -m ({m2})", color="green")
    plt.plot(x, mu_sum, label="Сума", color="red", linestyle="--")

    plt.title("Додавання нечітких чисел")
    plt.xlabel("x")
    plt.ylabel("Ступінь належності")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
