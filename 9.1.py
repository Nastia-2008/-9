from array import array
import random
min = int(input("Введіть мінімальне значення діапазону: "))
max = int(input("Введіть максимальне значення діапазону: "))
mas = array('i', [random.randint(min, max) for _ in range(10)])
print("масив:", mas.tolist())

sum_1= sum(mas[:5])
a_2 = sum(mas[5:]) / len(mas[5:])
print(f"Сума елементів першої половини масиву: {sum_1}")
print(f"Середнє арифметичне другої половини масиву: {a_2:.2f}")

s = int(input("Введіть число для пошуку: "))
if s in mas:
    print(f"Число {s} знайдено у масиві на позиції {mas.index(s)}.")
else:
    print(f"Число {s} у масиві не знайдено.")
