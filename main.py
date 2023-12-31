import iters
import velocity
def printInfo(iters, prev_x, df, cur_x, prev_step_size, velocity):
print("Iteration :", iters)
print("previous x :", prev_x)
print("gradient df:", df)
print("current x :", cur_x)
print("step size :", prev_step_size)
print("velocity :", velocity)
print()
cur_x = 5
#cur_x = 2
gamma = 0.001 # step size multiplier
precision = 0.000001
previous_step_size = 1
max_iters = 3 # maximum number of iterations
iters = 0 #iteration counter
momentum = 0.9
velocity = 0
df = lambda x: 6*x**2 + 12*x - 20
# df = lambda x: 4*x**3 - 40*x
# lists to store
iterations = []
step_size = []
while (previous_step_size > precision) & (iters < max_iters):
prev_x = cur_x
velocity = momentum * velocity + gamma * df(prev_x)
cur_x -= velocity
previous_step_size = abs(cur_x - prev_x)
iters+=1
printInfo(iters, prev_x, df(prev_x), cur_x, previous_step_size, velocity)
iterations.append(iters)
step_size.append(previous_step_size)
print("The local minimum occurs at:", cur_x)
