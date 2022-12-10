def prime_no(n):
    cnt=2
    for i in range(cnt,(n+1)):
        if n%cnt==0:
            break
        cnt=i
    if cnt==n:
        return (1)
    else:
        return (0)
ccnt=0
t=1
l=len(str(t))
no=t
while no<1000000:

            i = 0
            digit = 0
            reminder = 0
            sum = 0
            for i in range(i,l):

                reminder=no%10
                no=no/10
                no=int((reminder*(10**(l-1))+no))
                digit=prime_no(no)
                sum=sum+digit
                i=i+1

            if(sum==i):
                ccnt+=1
            t=t+1
            no=int(t)
print ("total=",ccnt)