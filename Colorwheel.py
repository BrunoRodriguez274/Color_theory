import numpy as np
import matplotlib.pyplot as plt



total_partition = 360



def create_color_wheel(n_):


    degs_ = np.linspace(0,360,n_)#*(np.pi)/180
    breaks = [degs_[int((i)*(n_/6))] for i in range(0,6)]
    breaks.append(360)


    print(breaks)
    cols =[]

    rgb = [0,0,255]

    break_count = 1
    for i in range(n_): 

        # Hasta el break
        
        if degs_[i] > breaks[break_count]:

            #print(degs_[i], breaks[break_count])
            
            break_count +=1

            mod = break_count%2

            print(i, break_count, mod)


        
        if break_count <=1:
            
            rgb[2- break_count+1] = 255

            rgb[2- break_count] = i* 4.25*360/n_ 

        else:
            
            if mod == 0:
                
                rgb[2- int(break_count/2)+1] = break_count*255 -(i* 4.25*360/n_ )


                rgb[2- int(break_count/2) ] = 255
            else:
                print((n_/break_count))
                rgb[2- int((break_count+1)/2)+1] = 255 

                rgb[2- int((break_count+1)/2) ] = (i - (break_count-1)*(n_/6))*4.25*360/n_ 
                
        angle_col =(rgb[0]/255, rgb[1]/255, rgb[2]/255)
        print(angle_col)

        cols.append(angle_col)

    return cols

#colors = create_color_wheel(total_partition)

#print(colors)

def plot_circle(n_):

    r = np.ones(n_)

    deg = np.linspace(0,360, n_)*(np.pi)/180
    x = r*np.sin(deg)
    y = r*np.cos(deg)

    colors = create_color_wheel(n_)

    print(len(x), len(colors))
    for i in zip(x, y, colors):
        


        plt.plot(i[0],i[1], '.', markersize = 30, color = i[2])
    plt.show()


plot_circle(50)
