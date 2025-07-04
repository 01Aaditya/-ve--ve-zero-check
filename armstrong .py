 for num in range(100, 1000): 
digits = [int(d) for d in str(num)] 
cube_sum = sum(d**3 for d in digits) 
if cube_sum == num: 
print(num)