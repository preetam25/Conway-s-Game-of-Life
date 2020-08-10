# Conway's Game of Life

![State Diagram](state_diagram.png)

## Instructions
1. Install dependencies - *Numpy*, *Matplotlib*   
`python3 -m pip install -r requirements.txt`
2. Start the game  
    * Random initialization  
`python3 gameOfLife.py`  
    * Custom initialization  
        * Add coordinates of live cells as new lines in the [input](input.txt)   
        `<y-coordinate> <x-coordinate>`  
        * `python3 gameOfLife.py input.txt`  


## Game Parameters
You can adjust the following parameters in the [code](gameOfLife.py) 
1. Size of the planet (*N*) 
2. Probability of life on the planet (*p*)
3. Animation interval (*interval*)

## Analysis
1. Time complexity **O**(*N*<sup>2</sup>)
2. Space complexity **O**(*N*<sup>2</sup>)

> ## [Preetam Pinnada](https://preetam25.github.io)
> Department of Electrical Engineering, IIT Bombay