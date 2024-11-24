def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print("Составное")
            return result
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)






#Результат консоли:
#Простое
#11



#Напишите 2 функции:
#Функция, которая складывает 3 числа (sum_three)
#Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в
# противном случае.#
#Примечания:
#Не забудьте написать внутреннюю функцию wrapper в is_prime
#Функция is_prime должна возвращать wrapper
#@is_prime - декоратор для функции sum_three