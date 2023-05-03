def loger(func):
    def wrapper(*args , **kwargs):
        rezult = func(*args , **kwargs)
        print(f"Функція: {func.__name__} , Аргумент: {args} , Резутальт: {rezult}")
        return rezult
    return wrapper
@loger
def example_fuction(a , b):
    return a + b
print(example_fuction(10 , 20))