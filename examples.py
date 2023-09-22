# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
#     print(arg1)
#     print(arg2)
#     print(arg3)


 
# Now we can use *args or **kwargs to
# pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)

def myFun(**kwargs):
    for key,value in kwargs.items():
        print(key,"==",value)
 
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)

# kwargs = {"name": "iranna", "age": "30", "gender": "male"}
# myFun(**kwargs)


# def hello_world_1(a, b=5, c=10, e={"name": "reddy"}, f={"age": 30}, *args, **kwargs):
#     print(args)
#     sum = (a,b,c)
#     # e = e
#     # # 
#     # f = f
#     print("name is: {} and age is: {}".format(e,f,c))
#     print(f"name is {e}, age is: {f}")
#     print(sum)
#     result = args+sum
#     return result
 
# hello_1 = hello_world_1(1,2,3,6,7,8,9,10) # sum of all these values
# print(hello_1) 