# basic decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wraper excuted this {} before.'.format(
            original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs):
#         print('call method excuted this {} before.'.format(
#             self.original_function.__name__))
#         return self.original_function(*args, **kwargs)

# @decorator_class
@decorator_function  # equivalent with line 24-25
def display():
    print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()


# @decorator_class
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))


display_info('John', 25)

display()
