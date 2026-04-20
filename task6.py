def log_methods(cls):
    for name, attr in cls.__dict__.items():
        if callable(attr):
            print(f"calling {name}")
    return cls
@log_methods
class Calculator:
    def add(self, a,b):
        return a+b
calc=Calculator()
calc.add(2,3)
