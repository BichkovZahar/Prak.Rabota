def finish(func):
    cache = {}
    def wrapper(*args , **kwars):
        if args in cache :
            return cache[args]
        else:
            rezult = func(*args)
            cache[args] = rezult
            return rezult , cache
    return wrapper
@finish
def example_function(x , y):
    return x * y
print(example_function(5 , 3))
