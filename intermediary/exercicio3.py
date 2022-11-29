def multiplica(multiplicador):
    def duplica(num1):
        return num1*multiplicador
    def triplica(num1):
        return num1*multiplicador
    def quadruplica(num1):
        return num1*multiplicador
    return duplica(2), triplica(3),quadruplica(4)

duplica= multiplica(2)
print(duplica)