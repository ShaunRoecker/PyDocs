import decimal
from decimal import Decimal
import math

# decimals 
# Decimals have a context that controls certain aspects of working with decimals
    # precision during arithmetic operations
    # rounding algorithm

#  This context can be global => the default context
#  or temporary(local) => sets temporary settings without affecting the global settings


global_context = decimal.getcontext()
print(global_context)
# Context(
#   prec=28, 
#   rounding=ROUND_HALF_EVEN, 
#   Emin=-999999, Emax=999999, 
#   capitals=1, 
#   clamp=0, 
#   flags=[], 
#   traps=[InvalidOperation, DivisionByZero, Overflow]
# )


local_context = decimal.localcontext(ctx=None)
print(local_context)
# returns a context manager(use a 'with' statement)


# Precision and Rounding:
ctx = decimal.getcontext() # context (global in this case)
ctx.prec  # get or set the precision (value is an int)
ctx.rounding # get or set the rounding mechanism(value is a string)


# Global 
# setting the context
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN


# Local
# use as context manager
with decimal.localcontext() as ctx:
    ctx.prec = 2
    ctx.rounding = decimal.ROUND_HALF_UP
    # anything you do in here will use this context

# it defaults back to global after you leave the context manager


g_ctx = decimal.getcontext()

print(type(g_ctx))  # <class 'decimal.Context'>

print(type(decimal.localcontext())) # <class 'decimal.ContextManager'>

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    # uses local context
    print(round(x, 1))    # 1.3
    print(round(y, 1))    # 1.4


# uses global context
print(round(x, 1))   # 1.2
print(round(y, 1))   # 1.3


# Constructors and Contexts
integers = Decimal(10)
strings = Decimal('0.1')
tuples = Decimal((1, (3, 1, 4, 1, 5), -4)) # -3.1415 Decimal((sign, (d,i,g,i,t,s), exponent))


print(tuples)


to_decimal = lambda x: Decimal(str(x))


decimal.getcontext().prec = 6

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)


# ****Dont create Decimals from floats*****
# create a string before passing to Decimal



decimal.getcontext().prec = 28
x = 0.01
x_dec = Decimal('0.01')
root = math.sqrt


# Div and Mod operators with Decimals

x = 10
y = 3

print(x//y, x%y)  # 3  1
print(divmod(x, y)) # (3, 1)
print(x == y * (x//y) + (x%y)) # True

a = Decimal(str(0.1))

print(a) # 0.1

print(format(a, '.35f')) # 0.10000000000000000000000000000000000



x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)



























