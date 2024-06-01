import math
while True:
    x = int(input("enter value(cos):"))
    angle = math.radians(x)
    cos_value = math.cos(angle)
    rounded_cos_value = round(cos_value, 2) 
    print("Cosine of " + str(x) + " degrees is:", rounded_cos_value)
    
    sin_value = math.sin(angle)
    rounded_sin_value = round(sin_value, 2)  
    print("Sine of " + str(x) + " degrees is:", rounded_sin_value)
    
    tan_value = math.tan(angle)
    rounded_tan_value = round(tan_value, 2)  
    print("Tangent of " + str(x) + " degrees is:", rounded_tan_value)