"""
input: no from the list
output: preceding and succeding numbers
"""
lst = [12,23,12,34,35,4,1,2,3,3,5,6,7,8,9,0]
n=0
ivn=0

def myfunction(n):
    for i in range(len(lst)):
        if lst[i]==n:
            ivn=i
            break
    print("you chossen no is : ",n)
    print("preceding number : ",end=" ")
    for item in lst[:ivn]:
        print(item,end=" ")

    print("\nsucceding number : ",end=" ")
    for item in lst[ivn+1:]:
        print(item,end=" ")           


if len(lst)==0:
    print("List is Empty")
    exit
else:   
    print(lst)
    n = int(input("choose Number from the above list:"))
    if n in lst:
        myfunction(n)
    else:
        print("choosen no is not in list ")




