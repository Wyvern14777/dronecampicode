from easytello import tello
d01e=tello.Tello()

d01e.takeoff()
d01e.up(50)
#d01e.forward(100)
for i in range (6):
      #d01e.left(60)
      #d01e.left(20)
      #d01e.right(60)
      #d01e.back(60)
      d01e.cw(180) 
      d01e.down(100)
      d01e.curve(x1= 30,y1= 30, z1= 20, x2= 100, y2= 170, z2= 100, speed= 30 )

d01e.land()
'''

d01e.takeoff()
for i in range(3):
      d01e.forward(50)
      d01e.right(40)
      d01e.forward(60)
      d01e.left(100)

d01e.cw(180)

for i in range(3):
      d01e.forward(50)
      d01e.right(40)
      d01e.forward(60)
      d01e.left(100)

d01e.takeoff()
for i in range (10):
      d01e.right(80)
      d01e.left(80)
      d01e.land()
      d01e.takeoff()

d01e.takeoff()
for i in range(3):
      height = 800 - d01e.get_tof()
      while height > 15:
            d01e.down(10)
            height = 800 - d01e.get_tof()
      d01e.forward(50)
d01e.land()

def bounce(d01e,bouncenumber):
      for i in range(bouncenumber):
            d01e.up(60)
            d01e.down(60)

d01e.takeoff()
bouncenumber = int(input("how many bounces"))
bounce(d01e,bouncenumber)

d01e.land()


num = int(input("how big (if circle dont go over 20, for your own safety)(in cm) "))
verticalorhorazontal = (input("vertical or horazontal if circle answer woln chang anything "))
if circorsqr == "square":
      if verticalorhorazontal == "horazontal":
            d01e.takeoff()
            d01e.left(num)
            d01e.back(num)
            d01e.right(num)
            d01e.forward(num)
            d01e.land()
      if verticalorhorazontal == "vertical":
            d01e.takeoff()
            d01e.left(num)
            d01e.up(num)
            d01e.right(num)
            d01e.down(num)
            d01e.land()
if circorsqr == "circle":
      d01e.takeoff()
      for i in range(36):
            d01e.forward(num)
            d01e.cw(10)
d01e.land()


for i in range(3):
      d01e.takeoff()
      d01e.forward(80)
      d01e.land()
'''














