#exercise1
name ='Rupanshi'
print(name)

#exercise2
number= 5
a= number%2
if a==0 :
     print("even number")
else:
     print("odd number")

#exercise3
for x in range(10):
     print(x+1)

#exercise4
numbers = [2,4,8,4,7,2]
sum=0
for number in numbers:
     sum += number

print(sum)

def calculate_function(x):
  y = x**3- 5*x*2+6*x+2
  return y

# This should print value for y=f(5)
print(calculate_function(5))