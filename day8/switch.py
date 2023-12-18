# p = 80

# match p:
#     case 80:
#         print("Distintion")
#     case 60:
#         print("First")
#     case 40:
#         print("Second")
#     case 30:
#         print("third")
#     case _:
#         print("failed")


p = 87

match p:
    case p if p>=80:
        print("Distintion")
    case p if p>=60:
        print("First")
    case p if p>=40:
        print("Second")
    case p if p>=30:
        print("third")
    case _:
        print("failed")
