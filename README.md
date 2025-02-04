This project is based on [Space-Time-AStar](https://github.com/GavinPHR/Space-Time-AStar.git), and the original code follows the MIT license.

# Space-Time A*
This is a space-time A* implementation for 3D grid maps.

## Mapping
In this implementation, the map needs to be converted into a non-zero integer grid map first.

## Distance Constraints
### Static Obstacles
The safe distance to static obstacles is predefined as the agent radius.

### Between Agents
The safe area between agents is defined as an ellipsoid, where the radius of the horizontal axis is twice the agent radius and the radius of the vertical axis is four times the agent radius.