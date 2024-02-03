import numpy as np
import matplotlib.pyplot as plt


def monte_carlo(func, a, b, num_points):

    x_points = np.random.uniform(a, b, num_points)
    y_points = func(x_points)

    return np.mean(y_points) * (b - a)


def func(x):
    return x**3 - 2*x**2 + 3*x + 1


a, b = -2, 2

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = func(x)

if __name__=='__main':

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^3 - 2x^2 + 3x + 1')
    plt.grid()
    plt.show()

    # Виведення результатів
    print(f'Значення інтеграла методом Монте-Карло: {monte_carlo(func, a, b, 10000)}')
