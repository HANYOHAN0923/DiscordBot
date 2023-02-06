def trace(func):
    def wrapper():
        print(func.__name__, 'START')
        func()
        print(func.__name__, 'END')
    return wrapper

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)
trace_world = trace(world)

trace_hello()
trace_world()

print()
print('=============== DECORATOR ===============')
print()

@trace
def deco_hello():
    print('hello')

@trace
def deco_world():
    print('world')

deco_hello()
deco_hello()