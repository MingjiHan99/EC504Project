------
AVL Tree Implementation 

- The ```insert``` method inserts a new key into the tree. 

- The ```delete``` method removes the key with the given value from the tree.

- The ```find``` method searches for a key with the given value.

- The ```delete``` method search and delete the key with given value.


------
Files


    .
    ├── AVLTree.py              # class defination of AVL tree
    ├── run.py                  # randomly generate an array and insert into an AVL tree, plot the time it takes
    ├── plot.png                # if you set plot when running run.py, the plot whill be saved as this
    └── README.md

-------
To run the run.py, use this command
```bash
python run.py --num 1000 --seed 10 --sleepTime 0.001 --plot 0
```
-------
Args

```python
--num 2000                  # size of the random array
--seed 42                   # seed for the random array
--sleepTime 0.001           # sleep time in the insert operation, to better fit the function
--plot 0                    # whether use matplotlib module to plot and save the result
```

-------
To run on the SCC and plot the result, use those commands:
```bash
module load miniconda
conda create --name avltree python=3.8
conda activate avltree python=3.8
pip install numpy matplotlib
python run.py --num 1000 --seed 10 --sleepTime 0.001 --plot 0
```

------
Output example 

![Figure_insertion](https://user-images.githubusercontent.com/92005749/236181132-9a768504-4fac-4a50-af31-b152370a501c.png)
