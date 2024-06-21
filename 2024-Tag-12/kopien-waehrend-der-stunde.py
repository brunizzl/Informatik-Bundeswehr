
import copy

version = 0 # <- zahl ändern für anderen fall

if version == 1:
    x = 2
    y = x
    print("adresse von x = ", id(x), ", adresse von y = ", id(y))
    x += 1
    print("x = ", x, ", y = ", y)
    print("adresse von x = ", id(x), ", adresse von y = ", id(y))



if version == 2:
    x = [1, 2, 3]
    y = x
    #y = x.copy()
    print("adresse von x = ", id(x), ", adresse von y = ", id(y))
    x[0] = 99999
    print("x = ", x, ", y = ", y)
    print("adresse von x = ", id(x), ", adresse von y = ", id(y))



if version == 3:
    x = [[1, 2, 3], [4, 5, 6]]
    y = x
    #y = copy.deepcopy(x)
    print("adresse von x = ", id(x), ", adresse von y = ", id(y))
    (x[0])[0] = 99999
    print("x = ", x, ", y = ", y)
    print("adresse von x = ", id(x), ", adresse von y = ", id(y))

    print("adressen in x = [", id(x[0]), ", ", id(x[1]), "]")
    print("adressen in y = [", id(y[0]), ", ", id(y[1]), "]")





















