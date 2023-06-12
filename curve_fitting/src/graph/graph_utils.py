
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from PIL import Image

img = np.asarray(Image.open('/home/sb/projects/curve_fitting/samples/fig.png'))


class graph:
    range_x = None
    range_y = None
    

    def __init__(self, x_range=[0,1], y_range=[0,1],image=np.empty((1, 1, 3), dtype=np.uint8)):
        self.range_x = x_range
        self.range_y = y_range
        self.real_graph = image
        self.cur_graph=image
        self.values_x=[]
        self.values_y=[]
        self.pixels_x=[]
        self.pixels_y=[]

        self.poly_fit_param=[]

        self.height, self.width, _ = self.real_graph.shape
    
    def show_real_image(self):
        plt.imshow(self.real_graph)
        plt.show()
    
    def show_cur_image(self):
        plt.imshow(self.cur_graph)       
        plt.show

    def print_ranges(self):
        print("X Range:", self.rangeX)
        print("Y Range:", self.rangeY)

    def append_point(self,pixel_x,pixel_y):
        self.pixels_x.append(pixel_x)
        self.pixels_y.append(pixel_y)
        x_val,y_val = self.map_coordinates(pixel_x,pixel_y)

        self.values_x.append(x_val)
        self.values_y.append(y_val)
        print(f"inserted {x_val} and {y_val} to the graph")

    def remove_point(self,x,y):
        lx=self.values.x
        ly=self.values.y

        if x in lx :
            index = lx.index(x)
            lx.remove(x)
            ly.pop(index)
            print("removed {x} and {y} to the from")
        else:
            print("point not found")

    def map_coordinates(self,x,y):
    # Calculate the scaling factors
        mapped_x = np.interp(x, [0,self.width], self.range_x)
        mapped_y = np.interp(y, [0,self.height], self.range_y)
        mapped_y = (self.range_y[1]-mapped_y) +self.range_y[0]
        
        return mapped_x, mapped_y
        