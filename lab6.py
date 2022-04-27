function = lambda x : (x-3)/ (x*x)
sum = sum + function(x)
print(function(2))
print(sum)

def calc(x):
    r = ((x) / (x + 2)) - 10

    if x == 0 :
        return 1

    else:
        return r * calc(x-1)
calc(2)
print(calc(2))

