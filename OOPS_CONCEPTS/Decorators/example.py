# decorator -- wraps another function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("🎊Added sprinkles🎊")
        func(*args, **kwargs)
    return wrapper

def add_choco_chips(func):
    def wrapper(*args, **kwargs):         #arrgs are passed to accept the arguments
        print("🍫Added Choco-chips🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_choco_chips           #any no.of decorators can be added
def get_icecream(flavour):
    print(f"Here is your {flavour} icecream🍨")

get_icecream("Vanilla")