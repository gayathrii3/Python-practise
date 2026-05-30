# Positional----> (non-key arguments), 
# Default arguments-----> (when there are no arguments while func calling)
# ------------------------------------------------------------------------------------------------


#============== keyword arguments================

# def get_phone(country_code, area, first, last):
#     return f"{country_code}--{area}-{first}-{last}"

# phone_num = get_phone(country_code='+91', area=982,first=892,last=8996)

# print(phone_num)

# --------------------------------------------------------------------
# =========================Arbitrary arguments========================(not known in advance)
# --------------------------------------------------------------------

# (*args) ---> allows to pass multiple non-key arguments (type = tuple)
# * is used for unpacking
# ====================================================================

# def add(*args):
#     total = 0

#     for n in args:
#         total += n

#     return total

# print(add(2, 5, 6, 7))

# ------------------------------------------------------------------------------------
# *kwargs-----> allows multiple keyword arguments while function calling  (type = dict)
# =====================================================================================

# def print_address(**kwargs):

#     for key, value in kwargs.items():
#         print(f"{key:7} : {value}")

# print_address(street = "Jeedimetla",
#                     City = "Hyderabad,",
#                     State = "Telangana",
#                     Zip = "500055")

# -------------------------------------------------------------------------------------
# write a program for shipping label using both *args & **kwargs

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('Street')} {kwargs.get('City')}")
    print(f"{kwargs.get('State')} {kwargs.get('Zip')}")


shipping_label("Miss", "Gayathri",
                Street = "43 Texas Academy",
                City = "Hyderabad",
                State = "Telangana",
                Zip = "500055")
