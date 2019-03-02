from matplotlib import pyplot
from matplotlib import animation
import numpy
import random
import math

# Plot setup
figure = pyplot.figure()
figure.suptitle('Cournot Market Simulation')

axes_1 = pyplot.subplot(1,3,1)
axes_2 = pyplot.subplot(1,3,2)
axes_3 = pyplot.subplot(1,3,3)

# Functions
def update(frame):
    axes_1.clear(), axes_2.clear(), axes_3.clear()
    standardize_axes()
    # Demand scatter
    demand1 = axes_1.scatter(frame['demand1'][0], frame['demand1'][1], c='red')
    demand2 = axes_2.scatter(frame['demand2'][0], frame['demand2'][1], c='red')
    demand3 = axes_3.scatter(frame['demand3'][0], frame['demand3'][1], c='red')
    # Demand best-fit coefficients
    fit1 = numpy.polyfit(frame['demand1'][0], frame['demand1'][1], 1)
    fit2 = numpy.polyfit(frame['demand2'][0], frame['demand2'][1], 1)
    fit3 = numpy.polyfit(frame['demand3'][0], frame['demand3'][1], 1)
    # Demand fit lines
    demand1_fit = axes_1.plot(frame['demand1'][0], numpy.poly1d(fit1)(frame['demand1'][0]))
    demand2_fit = axes_2.plot(frame['demand2'][0], numpy.poly1d(fit2)(frame['demand2'][0]))
    demand3_fit = axes_3.plot(frame['demand3'][0], numpy.poly1d(fit3)(frame['demand3'][0]))
    # Supply equilibriums
    eq1 = get_supply_eq(fit1[1], fit1[0])
    eq2 = get_supply_eq(fit2[1], fit2[0])
    eq3 = get_supply_eq(fit3[1], fit3[0])
    # Supply lines
    supply1 = axes_1.plot([0,eq1[0]], [0,eq1[1]], color='green')
    supply2 = axes_2.plot([0,eq2[0]], [0,eq2[1]], color='green')
    supply3 = axes_3.plot([0,eq3[0]], [0,eq3[1]], color='green')
    return demand1, demand2, demand3, \
            demand1_fit, demand2_fit, demand3_fit, \
            supply1, supply2, supply3

def frames():
    data1, data2, data3 = [(0,5),(5,0)], [(0,5),(5,0)], [(0,5),(5,0)]
    while True:
        curves = {
            'demand1': format(data1),
            'demand2': format(data2),
            'demand3': format(data3)
        }
        yield curves

def format(coordinates):
    x, y = [], []
    for i in coordinates:
        x.append(i[0])
        y.append(i[1])
    return (x,y)

def standardize_axes():
    for x in (axes_1, axes_2, axes_3):
        x.set_title('Market')
        x.set_xlabel('Quantity')
        x.set_ylabel('Price')
        #x.set_xlim(0,6)
        #x.set_ylim(0,6)
        #x.set_autoscale_on(False)

def get_supply_eq(y_int, slope):
    mc = 1
    cost_entry = 2
    n = (y_int-mc-math.sqrt(math.fabs(slope*cost_entry)))/(math.sqrt(math.fabs(slope*cost_entry)))
    quantity = (y_int-mc)/(math.fabs(slope)*n+math.fabs(slope))
    price = y_int-math.fabs(slope)*quantity
    return [quantity, price]

anim = animation.FuncAnimation(figure, update, frames=frames, interval=4000)
pyplot.show()
