ls=[]
def f(show,left,right,num):
    if left==num and right==num:
        ls.append(show)
        return ls
    else:
        if left<num:
            f(show+'(',left+1,right,num)
        if right<left:
            f(show+')',left,right+1,num)
n=int(input())
f("",0,0,n)
print(ls)
