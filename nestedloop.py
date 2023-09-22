# for table_value in range(1, 5):
#     for multiplier in range(1, 11):
#         answer = table_value * multiplier
#         print(answer, end=' ')
#     print()
# else:
#     print('For loop is over!')

for i in range(1,5):
    for j in range(1,i+1):
        print( end=f'{j }' + " ")
    print()   