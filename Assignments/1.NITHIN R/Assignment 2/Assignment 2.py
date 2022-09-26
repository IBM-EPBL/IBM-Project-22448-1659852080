import random
n=random.randint(0,100)
print(n)
print(" ")
for i in range(0,n):
  temperature=random.randint(0,100)
  humidity=random.randint(0,100)
  print("Temperature:",temperature)
  print("Humidity:",humidity)
  if temperature>=30:
    print("Alert💀💀: High temp!!!!!!!")
  elif temperature<30:
    print("Alert✨✨: Low temp!!!!!!!")

