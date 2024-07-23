from pylab import plot, show, axis, legend
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
incheon = [25.0, 27.5, 24.0, 29.0, 28.2, 25.0, 26.4, 28.0, 24.0, 28.0]
daegu = [27.2, 30.2, 25.0, 36.2, 35.1, 28.2, 30.1, 25.1, 23.2, 34.1]
plot(month, incheon, month, daegu)
axis()
axis(xmin=1, ymin=0)
legend(['Incheon', 'Daegu'], loc='best')
show()