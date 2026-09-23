# Коэффициенты перевода в метры
units = {
    "км": 1000,
    "м": 1,
    "см": 0.01,
    "мм": 0.001,
    "mi": 1609.344,
    "yd": 0.9144
}

print("Доступные единицы: км, м, см, мм, mi, yd")

src = input("Исходная единица: ").strip().lower()
dst = input("Целевая единица: ").strip().lower()

if src in units and dst in units:
    value = float(input("Значение для конвертации: "))
    result = value * units[src] / units[dst]
    print(f"{value} {src} = {result:.4f} {dst}")
else:
    print("Неизвестная единица измерения")
