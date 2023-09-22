def hello_world_1(a, b=5, c=10, *args):
    sum = (a,b,c) + args
    result=0
    for x in sum:
          result = result + x      
    return(result)
 
hello_1 = hello_world_1(1,2,3,4,5,6,7,8,9,10) 
print(hello_1) 

#PyGenicArc . https://www.geeksforgeeks.org/args-kwargs-python/

def hello_world_1(a, b=5, c=10, e={"name": "reddy"}, f={"age": 30}, *args, **kwargs):
    print(args)
    sum = (a,b,c)
    # e = e
    # # 
    # f = f
    print("name is: {} and age is: {}".format(e,f,c))
    print(f"name is {e}, age is: {f}")
    print(sum)
    result = args+sum
    return result
 
hello_1 = hello_world_1(1,2,3,6,7,8,9,10) # sum of all these values
print(hello_1) 