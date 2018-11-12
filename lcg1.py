
#LCG
a=5
c=9
m=128
seed=71
n=30
g=.4
y=.1
r=.5


def crunch(a,c,m,z):
    '''
     computes math
     (int) ->(int)
    '''
    x = (((a*z)+c) % m)
    return x


def gen(a,c,m,seed,n):
    '''
    performs LCG function n times, given the user params
    (int)->[(int),(int)]
    '''

    nums=[]
    

    for i in range(0,n):
        temp = crunch(a,c,m,seed)
        seed = temp
        nums.append(temp)

    return nums


def meanGen(nums):
    return sum(nums)/len(nums)

def varGen(nums):
    varRaw = 0
    mean = meanGen(nums)
    for i in range (0,len(nums)):
       varRaw = varRaw+((nums[i]-mean)**2)
    return varRaw/len(nums)


#drop this?

def normalize(nums):
    normalized =[]

##    traditional
    
##    Max = max(nums)
##    Min = min(nums)
##    denom = Max - Min
    
    for i in range(0,len(nums)):

##        traditional
##      numer =  nums[i] - Min
##      normdval = numer/denom

        normdval = nums[i]/m
        normalized.append(normdval)

    return normalized



def stoplight(nums,g,y,r):
    rCount = []
    yCount = []
    gCount = []
  
    for i in range(0,len(nums)):
        if nums[i] <= r :
            print('original value')
            print('normalized value')
            print(nums[i])
            print('stoplight colour')
            print('RED')
            print('-----')
            rCount.append(1)
        elif r < nums[i] <= r+g:
            print('original value')
            print('normalized value')
            print(nums[i])
            print('stoplight colour')
            print('GREEN')
            print('-----')
            gCount.append(1)

        else:
            print('original value')
            print('normalized value')
            print(str(nums[i]))
            print('stoplight colour')
            print('YELLOW')
            print('-----')
            yCount.append(1)

    print('number of RED ' + str(len(rCount)))
    print('number of GREEN ' + str(len(gCount)))
    print('number of YELLOW ' + str(len(yCount)))

    print('red porprtion')
    rp = len(rCount)/(len(rCount)+len(gCount)+len(yCount))
    print(str(rp))

    print('green porprtion')
    gp = len(gCount)/(len(rCount)+len(gCount)+len(yCount))
    print(str(gp))

    print('yellow porprtion')
    yp = len(yCount)/(len(rCount)+len(gCount)+len(yCount))
    print(str(yp))

    

def stoplightShort(nums,g,y,r,og):
    rCount = []
    yCount = []
    gCount = []
  
    for i in range(0,len(nums)):
        if nums[i] <= r :
            rCount.append(1)
        elif r < nums[i] <= r+g:

            gCount.append(1)

        else:
            yCount.append(1)

    print('number of RED ' + str(len(rCount)))
    print('number of GREEN ' + str(len(gCount)))
    print('number of YELLOW ' + str(len(yCount)))

    print('red porprtion')
    rp = len(rCount)/(len(rCount)+len(gCount)+len(yCount))
    print(str(rp))

    print('green porprtion')
    gp = len(gCount)/(len(rCount)+len(gCount)+len(yCount))
    print(str(gp))

    print('yellow porprtion')
    yp = len(yCount)/(len(rCount)+len(gCount)+len(yCount))
    print(str(yp))







print('--------')
print('n=30')
n = 30
x= gen(a,c,m,seed,n)
y = normalize(x)
mean = str(meanGen(y))
var = str(varGen(y))
print(' the mean is ' + mean)
print(' the var is ' + var)
stoplight(y,g,y,r)
print('--------')
##
##print('--------')
##print('n=300')
##n = 300
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##mean = str(meanGen(y))
##var = str(varGen(y))
##print(' the mean is ' + mean)
##print(' the var is ' + var)
####stoplight(y,g,y,r)
##print('--------')
##
##print('--------')
##print('n=3000')
##n = 3000
##x= gen(a,c,m,seed,n)
##mean = str(meanGen(y))
##var = str(varGen(y))
##print(' the mean is ' + mean)
##print(' the var is ' + var)
####stoplight(y,g,y,r)
##print('--------')
##
##print('--------')
##print('n=3000000')
##n = 3000000
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##mean = str(meanGen(y))
##var = str(varGen(y))
##print(' the mean is ' + mean)
##print(' the var is ' + var)
####stoplight(y,g,y,r)
##print('--------')

##
##print('--------')
##print('n=30')
##n=30
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##stoplightShort(y,g,y,r,x)
##print('--------')
##
##print('--------')
##print('n=300')
##n=300
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##stoplightShort(y,g,y,r,x)
##print('--------')
##
##print('--------')
##print('n=3000')
##n=3000
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##stoplightShort(y,g,y,r,x)
##print('--------')
##
##print('--------')
##print('n=30000')
##n=30000
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##stoplightShort(y,g,y,r,x)
##print('--------')
##
##print('--------')
##print('n=300000')
##n=300000
##x= gen(a,c,m,seed,n)
##y = normalize(x)
##stoplightShort(y,g,y,r,x)
##print('--------')


##






 
