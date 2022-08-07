import zmq
import time
import math

print("Made by Cas Truyers!!!")

context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.connect("tcp://192.168.69.40:5555")
str1 = "deltaRobot>Move>"
str2 = ""
str3 = "-310>100:50:50>"
r = 70  # Straal in coordinaten

# The lower this value the higher quality the circle is with more points generated
stepSize = 0.15

for i in range(0, 2):
    t = 0
    while t < 2 * math.pi:
        x = (r * math.cos(t))
        y = (r * math.sin(t))
        str2 = str(x) + ':' + str(y) + ':'
        sender.send_string(str1 + str2 + str3 + "\n")
        t += stepSize


print("Done")

time.sleep(3)
