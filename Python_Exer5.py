x = 0

result = []


while x < 100:
    x +=1
    if x%5==0 and x%3 ==0:
        result.append("FizzBuzz")
    if x%3==0:
        result.append("Fizz")
    elif x%5==0 :
        result.append("Buzz")
    else:
        result.append(x)
        
print(result)