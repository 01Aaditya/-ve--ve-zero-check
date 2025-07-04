dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
merged_dict = {}
for key in dict1:
    merged_dict[key] = dict1[key]
for key in dict2:
    if key in merged_dict:
        merged_dict[key] += dict2[key]  
    else:
        merged_dict[key] = dict2[key]   
print("Merged dictionary with summed values:")
print(merged_dict)