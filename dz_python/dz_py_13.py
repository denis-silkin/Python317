# Homework_13

# def para(a, b, c):
#     def rect(x, y):
#         return x * y
#
#     s = 2 * (rect(a, b) + rect(a, c) + rect(b, c))
#     return s
#
#
# print(para(2, 4, 6))
# print(para(5, 8, 2))
# print(para(1, 6, 8))

# -----------------------------------------

# s = 0
#
#
# def para(a, b, c):
#     def rect(x, y):
#         return x * y
#
#     global s
#     s = 2 * (rect(a, b) + rect(a, c) + rect(b, c))
#     return s
#
#
# para(2, 4, 6)
# print(s)
# para(5, 8, 2)
# print(s)
# para(1, 6, 8)
# print(s)

# ---------------------------------------------------

def para(a, b, c):
    s = 0

    def rect(x, y):
        nonlocal s
        s += x * y

    rect(a, b)
    rect(a, c)
    rect(b, c)
    return 2 * s


print(para(2, 4, 6))
print(para(5, 8, 2))
print(para(1, 6, 8))
