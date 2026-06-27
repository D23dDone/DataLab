import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Индивидуальное задание SimpleAnalysis
# Язык: Python
# Библиотеки: Math, Matplotlib, Pandas, Numpy
# ------------------------------------------------------------


def round_to_hundreds_math(value: int) -> int:
    """
    Округление числа до сотен по математическому правилу.
    Например:
    149 -> 100
    150 -> 200
    -149 -> -100
    -150 -> -200
    """
    sign = 1 if value >= 0 else -1
    abs_value = abs(value)
    rounded = math.floor(abs_value / 100 + 0.5) * 100
    return sign * rounded


# ------------------------------------------------------------
# 1. Получить Dataset
# ------------------------------------------------------------

# Генерируем 1000 целых случайных чисел в диапазоне от -10000 до 10000
np.random.seed(42)  # чтобы при каждом запуске получался одинаковый результат

numbers = np.random.randint(-10000, 10001, size=1000)

# Формируем объект Series
data_series = pd.Series(numbers, name="Исходные значения")


# ------------------------------------------------------------
# 2. Рассчитать стандартные числовые характеристики Series
# ------------------------------------------------------------

min_value = data_series.min()
max_value = data_series.max()
sum_value = data_series.sum()
std_value = data_series.std()

# Количество значений, которые встречаются повторно
# Например, если число 15 встретилось 3 раза, оно считается как одно повторяющееся значение
repeated_values_count = data_series[data_series.duplicated()].nunique()

# Дополнительно: сколько всего элементов являются повторениями
# Например, если число 15 встретилось 3 раза, то повторов будет 2
total_repeated_elements = data_series.duplicated().sum()


print("СТАНДАРТНЫЕ ЧИСЛОВЫЕ ХАРАКТЕРИСТИКИ НАБОРА ДАННЫХ SERIES")
print("-" * 70)
print(f"Минимальное значение: {min_value}")
print(f"Максимальное значение: {max_value}")
print(f"Сумма чисел: {sum_value}")
print(f"Среднеквадратическое отклонение: {std_value:.2f}")
print(f"Количество повторяющихся значений: {repeated_values_count}")
print(f"Количество повторных элементов: {total_repeated_elements}")
print("-" * 70)


# ------------------------------------------------------------
# 3. Визуализировать исходные данные
# ------------------------------------------------------------

# Линейный график исходных данных
plt.figure(figsize=(12, 6))
plt.plot(data_series.index, data_series.values)
plt.title("Линейный график исходного набора данных")
plt.xlabel("Индекс элемента")
plt.ylabel("Значение")
plt.grid(True)
plt.show()


# Округляем значения набора данных до сотен по математическому правилу
rounded_series = data_series.apply(round_to_hundreds_math)

# Гистограмма округлённых значений
plt.figure(figsize=(12, 6))
plt.hist(rounded_series, bins=30, edgecolor="black")
plt.title("Гистограмма значений, округлённых до сотен")
plt.xlabel("Округлённые значения")
plt.ylabel("Количество элементов")
plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 4. Сформировать DataFrame из Series и добавить столбцы
# ------------------------------------------------------------

sorted_ascending = data_series.sort_values(ascending=True).reset_index(drop=True)
sorted_descending = data_series.sort_values(ascending=False).reset_index(drop=True)

df = pd.DataFrame({
    "Исходные значения Series": data_series,
    "Отсортированные по возрастанию": sorted_ascending,
    "Отсортированные по убыванию": sorted_descending
})


print()
print("DATAFRAME С ИСХОДНЫМИ И ОТСОРТИРОВАННЫМИ ДАННЫМИ")
print("-" * 70)
print(df)
print("-" * 70)


# ------------------------------------------------------------
# 5. Визуализировать данные после промежуточного анализа
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df.index,
    df["Отсортированные по возрастанию"],
    label="Отсортированные по возрастанию"
)

plt.plot(
    df.index,
    df["Отсортированные по убыванию"],
    label="Отсортированные по убыванию"
)

plt.title("Два линейных графика отсортированных значений")
plt.xlabel("Индекс элемента")
plt.ylabel("Значение")
plt.legend()
plt.grid(True)
plt.show()