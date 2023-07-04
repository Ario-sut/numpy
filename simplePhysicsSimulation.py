import numpy as np

def main():
    # create numpy array
    pos = np.zeros(2)
    vel = np.zeros(2)

    # Set the initial position
    pos[0] = 0
    pos[1] = 0

    # set initial velocity
    vel[0] = 5
    vel[1] = 5

    # simulate the motion of the object
    for v in range(10):
        pos+= vel
        vel -= np.array([0.1,0.1])
    # Print the final position & velocity
    print(pos)
    print(vel)

if __name__ == "__main__":
    main()