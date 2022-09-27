import random 
p=random.randint(0,50)
print(p)
print(" ")
for i in range(0,p):
  temp=random.randint(0,50)
  humi=random.randint(0,50)
  print("Temp:",temp)
  print("Humi:",humi)
  if temp>=30:
    print("hazardous!!!!!!!")
  elif temp<30:
    print("normal!!!!!!!")