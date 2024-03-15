import random
from collections import Counter
import pandas as pd


def simulate_dice_rolls(num_rolls):
    rolls_counter = Counter()
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        rolls_counter[dice1 + dice2] += 1
    return rolls_counter


def calculate_probabilities(rolls_counter, num_rolls):
    probabilities = {i: rolls_counter[i] / num_rolls * 100 for i in range(2, 13)}
    return probabilities


# Кількість кидків кубиків для симуляції
num_rolls = 100000

# Симуляція кидків кубиків
rolls_counter = simulate_dice_rolls(num_rolls)

# Обчислення ймовірностей
probabilities = calculate_probabilities(rolls_counter, num_rolls)

# Очікувані імовірності з таблиці
expected_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Створення DataFrame
data = {'Сума': list(probabilities.keys()),
        'Імовірність (Монте-Карло)': [f'{probabilities[i]:.2f}% ({rolls_counter[i]}/{num_rolls})' for i in probabilities.keys()],
        'Очікувана імовірність': [f'{expected_probabilities[i]:.2f}%' for i in probabilities.keys()]}
df = pd.DataFrame(data)

# Виведення таблиці
print(df)
