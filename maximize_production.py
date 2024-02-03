from pulp import LpMaximize, LpProblem, LpVariable

# Створення проблеми оптимізації
problem = LpProblem(name="Maximize production", sense=LpMaximize)

# Оголошення змінних рішення
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Додавання обмежень
problem += 2 * lemonade + fruit_juice <= 100  # вода
problem += lemonade <= 50  # цукор
problem += lemonade <= 30  # лимонний сік
problem += 2 * fruit_juice <= 40  # фруктове пюре

# Додавання об'єктивної функції для максимізації
problem += lemonade + fruit_juice

# Розв'язання проблеми
problem.solve()

# Виведення результатів
print(f"Кількість лимонаду: {lemonade.varValue}")
print(f"Кількість фруктового соку: {fruit_juice.varValue}")
