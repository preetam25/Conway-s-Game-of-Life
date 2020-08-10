import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Size of the planet
N = 50
# Probability of life on the planet
p = 0.2 
# Animation parameters
interval = 50 

# Window to look out for neighbors
window = np.array([[1,1,1],[1,0,1],[1,1,1]])

# Create a new world!
grid = np.random.choice([0,1], size=[N+2,N+2], p=[1-p,p]) 

# Update after every generation
def update(frameNum, img, grid, N): 
	
	temp = grid.copy() 
	
	for i in range(1, N+1): 
		for j in range(1, N+1): 
			
			# Count number of neighbors
			neighbors = np.einsum('ij,ij', grid[i-1:i+2,j-1:j+2], window)	
			
			# Conway's rules 
			if neighbors == 3: temp[i,j] = 1
			elif neighbors != 2: temp[i, j] = 0
	
	# No life at borders
	temp[0] = np.zeros([1,N+2])
	temp[N+1] = np.zeros([1,N+2])
	temp[:,0] = np.zeros(N+2)
	temp[:,N+1] = np.zeros(N+2)
	
	# Update frame
	img.set_data(temp) 
	grid[:] = temp[:] 
	return img, 

fig, ax = plt.subplots() 
img = ax.imshow(grid, cmap='Greens') 
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), interval=interval) 
plt.axis('off')
plt.show() 