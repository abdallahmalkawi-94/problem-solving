# from numpy import *
#
# customers = array([[1,2,3],[4,5,6],[7,8,9]])
# customers_amount = []
# for customer in customers:
#     customers_amount.append(sum(customer))
#
# print(max(customers_amount))

customers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
max = 0
for customer in customers:
    if sum(customer) > max:
        max = sum(customer)

print(max)