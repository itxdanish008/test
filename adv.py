# lambda arg : expression
lst = [1,2,3,4]
# letsee = lambda num : "Even" if num%2==0 else 'Odd'
letsee2 = list(filter(lambda x : x%2 !=0, lst)) 

print(letsee2)