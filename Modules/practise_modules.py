# Modules   ----> a file containing code that u wants to use in your program 
                # (import ----> to include a module(built-in or your own))

# ----> import math
# ----> import math as m
# ----> from math import pi 
# ===========================================================================

# import math

# print(f"{math.pi:2f}")

# ---------------------------------------------------------------------------

# print(help("modules"))

# ---------------------------------------------------------------------------

# import math

# a, b, c = 1, 2, 3

# print(f"{math.pi ** a:.2f}")
# print(math.e ** b)
# print(math.pi ** c)

# --------------------------------------------------------------------------
#  imported (buit-in) module from another file(create_module.py)

import create_module

results = create_module.pi

results = create_module.square(56)
# results = create_module.circumference(20)

print(f"{results:.2f}")
