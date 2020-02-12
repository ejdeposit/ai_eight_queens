def foo(dict):
    dict[0]=1

def change_tuple(t):
    t=(1,1)

dict={}
dict[0]=2
print(dict[0])
foo(dict)
print(dict[0])

blankLoc=(0,0)
print(blankLoc)
change_tuple(blankLoc)
print(blankLoc)
