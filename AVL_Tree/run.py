from AVLTree import AVLTree
import random
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num', default=2000, help='length of a random array')
parser.add_argument('--seed', default=42, help='seed for the random array')
parser.add_argument('--sleepTime', default=0.001, help='sleep time in insertion')
parser.add_argument('--plot', default=0, help='save plot via matplot or not')

args = parser.parse_args()

if int(args.plot):
    import matplotlib.pyplot as plt
    
N = int(args.num)  # Replace 10 with the desired length of the array
sleep_time = float(args.sleepTime)
random.seed(int(args.seed))  # Replace 42 with the desired seed value

times = [] # count time
x = []
array = [random.random() for i in range(N)] # Generate a list of N random numbers between 0 and 1

print("Building...")
tree = AVLTree(sleep_time)

for i in range(N):
    start_time = time.time()
    tree.insert(array[i])
    if i % 10 == 0:
        x.append(i+1)
        times.append(time.time() - start_time)
    
print("Done.")
print("Tree height: " + str(tree.height(tree.root)))


if int(args.plot):
    plt.plot(x, times, marker='o', linestyle='none', label='AVL insertion')
    plt.plot(x, np.log(x)/450, label='logN')
    plt.legend()
    plt.xlabel('Num')
    plt.ylabel('Time')
    plt.savefig('plot.png')
