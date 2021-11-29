def kvadratiniAl(func):
    def inner():
        eded=func()
        return eded**2
    return inner

@kvadratiniAl
def Method02():
    return 10

def EdedIstehsalEt():
    return 5

decorator=kvadratiniAl(Method02)
print(decorator())