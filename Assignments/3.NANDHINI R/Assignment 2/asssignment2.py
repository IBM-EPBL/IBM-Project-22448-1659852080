import random
temp=random.randint(0,100)
print(temp)
import random
hum=random.randint(0,100)
print(hum)
if temp >75:
    if hum >75:
        print("Hazard predected")

    else:
        print("No hazard")

elif temp==75:
     print ( "High temperature")

else:
    print("All good")
