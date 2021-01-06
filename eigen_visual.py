



from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import numpy as np



x_first = np.linspace(0, 1, 1000)
# Just pythagoras
y = lambda x: np.sqrt(1 - x**2)

# New fun way to drawing a circle
circle_points = np.array([ np.concatenate([-x_first, -x_first, x_first, x_first]) , np.concatenate([y(x_first), -y(x_first), -y(x_first), y(x_first)]) ])


eigen_vectors = np.array([1, 1]).T


# Set plot window
DPI = 150
width, height = 750, 750
fig = plt.figure(figsize=(width/DPI, height/DPI), dpi=DPI)

# Create main axis
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.25, top=0.75)
plt.axis([-3.1, 3.1, -3.1, 3.1])


# def circle_transformation(e_value, e_vector, circle):
def circle_transformation(e_value, e_vector, circle):
	circle = np.array([np.dot(circle[:,i], e_value) for i in range(circle.shape[1])]).T
	circle = np.array([np.dot(circle[:,i], e_vector) for i in range(circle.shape[1])]).T
	return(circle)




# Create axes for sliders
ax_Eigen1 = fig.add_axes([0.325, 0.90, 0.4, 0.025])
ax_Eigen1.spines['top'].set_visible(True)
ax_Eigen1.spines['right'].set_visible(True)
ax_Eigen2 = fig.add_axes([0.325, 0.95, 0.4, 0.025])
ax_Eigen2.spines['top'].set_visible(True)
ax_Eigen2.spines['right'].set_visible(True)
ax_Rotationv1 = fig.add_axes([0.325, 0.85, 0.4, 0.025])
ax_Rotationv1.spines['top'].set_visible(True)
ax_Rotationv1.spines['right'].set_visible(True)
ax_Rotationv2 = fig.add_axes([0.325, 0.80, 0.4, 0.025])
ax_Rotationv2.spines['top'].set_visible(True)
ax_Rotationv2.spines['right'].set_visible(True)



# Create sliders
s_Eigen1 = Slider(ax=ax_Eigen2, label='Eigenvalue 2 ', valmin=0, valmax=3.0,
              facecolor='#cc7000')
s_Eigen2 = Slider(ax=ax_Eigen1, label='Eigenvalue 1 ', valmin=0, valmax=3.0, 
             facecolor='#cc7000')

s_Rotationv1 = Slider(ax=ax_Rotationv2, label='Rotationvector 2 ', valmin=0, valmax=2*np.pi,
              facecolor='#cc7000', valinit = 0)
s_Rotationv2 = Slider(ax=ax_Rotationv1, label='Rotationvector 1 ', valmin=0, valmax=2*np.pi, 
             facecolor='#cc7000', valinit = 0)




new_circle = circle_transformation(np.array([[ 0.5, 0 ], [ 0, 0.5 ]]), np.array([[ np.cos(0), -np.sin(0) ], [ np.sin(0), np.cos(0) ]]), circle_points )
interactive_plot = ax.scatter(new_circle[0], new_circle[1], s= 0.25)

# Update values
def update(val):
    Eigen2 = s_Eigen2.val
    Eigen1 = s_Eigen1.val
    Rotationv2 = s_Rotationv2.val
    Rotationv1 = s_Rotationv1.val
    interactive_plot.set_offsets(circle_transformation(np.array([[ Eigen2, 0 ], [ 0, Eigen1 ]]), np.array([[ np.cos(Rotationv1), -np.sin(Rotationv1) ], [ np.sin(Rotationv2), np.cos(Rotationv2) ]]), circle_points ).T)
    fig.canvas.draw_idle()
s_Eigen2.on_changed(update)
s_Eigen1.on_changed(update)
s_Rotationv2.on_changed(update)
s_Rotationv1.on_changed(update)



# Unit circle
ax.scatter(circle_points[0], circle_points[1], s= 0.25)
plt.show()


