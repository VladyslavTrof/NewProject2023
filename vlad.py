# Оголошуємо функцію, яка приймає список цілих чисел як параметр
def sum_even_and_multiply (lst):
  # Якщо список порожній, повертаємо 0
  if not lst:
    return 0
  # Ініціалізуємо змінну для зберігання суми елементів з парними індексами
  even_sum = 0
  # Проходимо по всіх елементах списку, використовуючи індексацію
  for i in range(len(lst)):
    # Якщо індекс парний, додаємо елемент до суми
    if i % 2 == 0:
      even_sum += lst[i]
  # Повертаємо добуток суми і останнього елемента списку
  return even_sum * lst[-1]

# Тестуємо функцію на прикладах
print(sum_even_and_multiply([0, 1, 7, 2, 4, 8])) # 88
print(sum_even_and_multiply([1, 3, 5])) # 30
print(sum_even_and_multiply([6])) # 36
print(sum_even_and_multiply([])) # 0
