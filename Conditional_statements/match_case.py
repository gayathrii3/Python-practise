# can be used as (switch-case) in th place of multiple elif statements

# def week(day):
#     match day:
#         case 1:
#             return "it's SUNDAY"
#         case 2:
#             return "it's MONDAY"
#         case 3:
#             return "it's TUESDAY"
#         case 4:
#             return "it's WEDNESDAY"
#         case 5:
#             return "it's THURSDAY"
#         case 6:
#             return "it's FRIDAY"
#         case 7:
#             return "it's SATURDAY"
#         case _:
#             return "Not a valid DAY"
        
# print(week(5))

# -----------------------------------------------------------

def is_completed(todo):
    match todo:
        case "Python" | "SQL":
            return "Partially completed"
        case "REST API" | "DSA":
            return "Not completed"
        case _:
            return "Exceeding limit"
        
print(is_completed("DSA"))