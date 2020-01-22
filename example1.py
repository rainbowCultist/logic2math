from components import Not, And, Or, Xor

from components import Input

a = Input(1, 'x')
b = Input(1, 'y')
c = Input(1, 'z')

test = And(Not(And(a[0], b[0])), Not(c[0]))

print(test.convert_latex())
