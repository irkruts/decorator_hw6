def decorator(fn):
    def wrapper(*args):
        print(f'FUNCTION NAME: {fn.__name__} ,with arguments: {args}')
        fn()

    return wrapper


@decorator
def just_a_function(*args):
    pass


just_a_function(4, 5, 6)
