import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create array of 100 random numbers
    data = np.random.rand(100)

    # Plot the data
    plt.plot(data)

    # Add a title
    plt.title("random data")

    # Add xy axis labels
    plt.xlabel('Index')
    plt.ylabel('Value')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()