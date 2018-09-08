def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(raw_input())
exp=int(raw_input())
print power(base,exp)
