#count e um iterador sem fim (itertools)

from itertools import count


c1 = count()

print(next(c1), hasattr(c1, '__iter__'))
print(next(c1))