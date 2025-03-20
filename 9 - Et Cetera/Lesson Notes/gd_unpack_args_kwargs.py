# UNPACKING WITH *ARGS AND **KWARGS

def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

# args
f(100, 50, 25)

# kwargs
f(galleons=100, sickles=50, knuts=25)