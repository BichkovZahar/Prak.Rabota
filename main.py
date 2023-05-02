def example_faction(func):
    def wrapper(*args , **kwargs):
        finish = func(*args , **kwargs) + 10
        return finish
    return wrapper
@example_faction
def rezult(args):
    return args
print('Результат:' , rezult(13))