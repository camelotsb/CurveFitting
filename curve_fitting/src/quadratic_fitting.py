from graph.graph_utils import *
from scipy.optimize import curve_fit


img = np.asarray(Image.open('/home/sb/projects/curve_fitting/samples/fig.png'))

grob = graph([0.5,1.75],[1.440,1.456],img)

def quad(x,a0,a1,a2):
    return a0 + a1*x + a2*(x**2)

def plot_fit():
    par, var = curve_fit(quad, np.array(grob.values_x), np.array(grob.values_y))
    grob.poly_fit_param=par
    par=par[::-1]

    x = np.linspace(grob.range_x[0], grob.range_x[1], 100)
    y = np.polyval(par, x)

    fig, ax = plt.subplots(1, 2)


    ax[0].set_xlim(grob.range_x)
    ax[0].set_ylim(grob.range_y)

    ax[0].plot(x, y)
    
    # Set labels and title
    ax[0].set_xlabel('X')
    ax[0].set_ylabel('Y')
    ax[0].set_title('Polynomial Plot')

    ax[1].imshow(grob.real_graph)
    ax[1].text(20, 20, str(par[0])+'x^2 +'+str(par[1])+'x +'+str(par[2]), fontsize=12, color='red')
    ax[1].set_title("Direct Image")

    plt.show()


def onclick(event):
    # print(event)
    # print("Pixel Coordinates: x = {}, y = {}".format(int(event.xdata), int(event.ydata)))
    x_val,y_val = grob.map_coordinates(event.xdata,event.ydata)

    if event.dblclick==False :
        print("Pixel Coordinates: x = {}, y = {}".format(int(event.xdata), int(event.ydata)))
        print(f"point coordinates: x = {x_val} and y = {y_val} ")

    else :
        grob.append_point(int(event.xdata),int(event.ydata))
        print(grob.values_x,'\n',grob.values_y)

        plt.plot(event.xdata, event.ydata, 'ro')  # 'ro' specifies red circles for the points
        plt.draw()
       
        # grob.cur_graph = grob.real_graph

plt.imshow(grob.cur_graph)

plt.gcf().canvas.mpl_connect('button_press_event', onclick)

plt.show()

plot_fit()




