# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

weight_as_integer = int(weight)
height_as_float = float(height)

bim = int(weight_as_integer / height_as_float ** 2)

print(bim)