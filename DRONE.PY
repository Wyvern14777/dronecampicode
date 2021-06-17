from easytello import tello
d01e=tello.Tello()
'''
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
'''
d01e.takeoff()
for i in range (10):
      d01e.right(80)
      d01e.up(80)
      d01e.land()
      d01e.takeoff()