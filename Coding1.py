
def fib(num):
    res=[]
    even_sum=0
    for i in range(num):
        if i==0:
            res.append(i+1)
            #print(res)
        else:
            if i==1:
                temp=res[-1]+1
                res.append(temp)
                if temp%2==0:
                    even_sum+=temp
            else:
                temp=res[-1]+res[-2]
                res.append(temp)
                if temp%2==0:
                    even_sum+=temp
    return even_sum
    
if __name__ == "__main__":
    for i in range(80):
        temp=fib(i)
        #print(temp)
        if(temp>4000000):
            print(temp)
            break
        