def decorator(fn):
    def wrapper(*args, **kwargs):
        print(f'FUNCTION NAME: {fn.__name__} ,with arguments: {args}')
        return fn(*args, **kwargs)

    return wrapper


@decorator
def just_a_function(a, b):
    return a - b + 10


print(just_a_function(4, 5))
