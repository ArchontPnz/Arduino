import serial
from matplotlib import pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=5)
ser.flush()

x_len = 200
y_range = [-3, 3]

fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1)
plt.title("x")
plt.ylabel("Acceleration")
plt.xlabel("Time")
ax2 = fig.add_subplot(1, 3, 2)
plt.title("y")
plt.ylabel("Acceleration")
plt.xlabel("Time")
ax3 = fig.add_subplot(1, 3, 3)
plt.title("z")
plt.ylabel("Acceleration")
plt.xlabel("Time")
xs = list(range(0, 200))
ys1 = [0] * x_len
ys2 = [0] * x_len
ys3 = [0] * x_len
ax1.set_ylim(y_range)
ax2.set_ylim(y_range)
ax3.set_ylim(y_range)

line1, = ax1.plot(xs, ys1)
line2, = ax2.plot(xs, ys2)
line3, = ax3.plot(xs, ys3)

#samples = 200
#data = []
#for i in range(1, samples):
    #val = float(ser.readline().rstrip())
    #if val:
        #data.append(val)
#    print(val)

#plt.plot(data)

plt.suptitle("Grapsh of acceleration")
plt.xticks(rotation=45, ha='right')
#plt.xlabel("Samples che-to tam")
#plt.savefig("gg.png")
#print(data)
#ser.close()

def animate(i, ys1, ys2, ys3):
    try:
        val1 = float(ser.readline().rstrip())
        val2 = float(ser.readline().rstrip())
        val3 = float(ser.readline().rstrip())
        valend = ser.readline()
        ys1.append(val1)
        ys2.append(val2)
        ys3.append(val3)

    except ValueError:
            print('Bad value')

    ys1 = ys1[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]

    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)

    return line1, line2, line3

ani = animation.FuncAnimation(fig, animate, fargs=(ys1, ys2, ys3), interval=10, blit=True)

print(line1)

#ani2 = animation.FuncAnimation(fig, animate, fargs=(ys2,), interval=10, blit=True)

plt.show()

ser.close()
