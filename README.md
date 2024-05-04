# Welcome to Pacman
After downloading the code (search.zip), unzipping it, and changing to the directory, you should be
able to play a game of Pacman by typing the following at the command line:
``` python pacman.py ```
Note: The exact command you should be using depends on your distribution and python installation.

Note that pacman.py supports a number of options that can each be expressed in a long way (e.g.,
--layout) or a short way (e.g., -l). You can see the list of all options and their default values via:
``` python pacman.py -h ```

## Depth First Search
``` python pacman.py -l tinyMaze -p SearchAgent ```
```python pacman.py -l mediumMaze -p SearchAgent ```
``` python pacman.py -l bigMaze -z .5 -p SearchAgent ```

## Breadth First Search
```python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs ```
```python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 ```

## Varying the Cost
```python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs ```
```python pacman.py -l mediumDottedMaze -p StayEastSearchAgent ```
```python pacman.py -l mediumScaryMaze -p StayWestSearchAgent ```

## A* Search 
```python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar ,heuristic = manhattanHeuristic ```

## Finding all corners
```python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs , prob = CornersProblem```
```python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs , prob = CornersProblem```

## Corners Problem: Heuristic
```python pacman.py -l mediumCorners -p AStarCornersAgent -z 0 .5```
Can also be written with
```-p SearchAgent -a fn= aStarSearch , prob = CornersProblem , heuristic = cornersHeuristic```

#Eating all dots
```python pacman.py -l testSearch -p AStarFoodSearchAgent```
```python pacman.py -l trickySearch -p AStarFoodSearchAgent```

#Suboptimal Search - Greedy
```python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5```
