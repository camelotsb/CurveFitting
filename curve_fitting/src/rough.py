import matplotlib.pyplot as plt
from PIL import Image

def plot_points_on_image(image_path, points):
    # Load the image
    image = Image.open(image_path)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(image)

    # Extract x and y coordinates from points
    x_coords, y_coords = zip(*points)

    print(x_coords)
    # Plot the points on the image
    ax.plot(x_coords, y_coords, 'ro')  # 'ro' specifies red circles for the points

    # Show the plot
    plt.show()

# Example usage:
image_path = '/home/sb/projects/curve_fitting/samples/fig.png'
points = [(100, 200), (300, 400), (500, 600)]

plot_points_on_image(image_path, points)
