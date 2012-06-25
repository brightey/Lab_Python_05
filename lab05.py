#the factorial question
def factorial(x):
 if(x<0):
  print 'you can not find factorial of a negative number'
 else:
  f=1
 while (x > 0):
        f = f * x
        x= x - 1
 return f


integ=raw_input('enter an integer:')
integ=int(integ)
 
print factorial(integ)

#fibonacci

def fibonacci(y):
    fi_li=[]
    for i in range(1,y+1):
        fi_li.append(fibon(i))
    return fi_li

integerr=raw_input('enter an integer:')
integerr=int(integerr)

print fibonacci(integerr)

def fibon(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibon(x-1)+fibon(x-2)


      
 


print fibonacci(integerr)




#prime
def prime(numm)
 if(numm%2==1)
  return 'true'
 else
   return 'false'



num=raw_input('enter an integer:')
num=int(num)
print prime(num)




  
  
 
 
