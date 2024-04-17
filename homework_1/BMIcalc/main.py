height = int(input("Please input ypur height"))
weight = int(input("Please input ypur weight"))
bmi = weight / (height / 100) ** 2
print("your height:"+str(height))
print("your weight:"+str(weight))
print("your bmi:"+str(round(bmi,2)))
