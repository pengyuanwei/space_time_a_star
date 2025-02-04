#!/usr/bin/env python3
'''
Modified based on [Space-Time-AStar](https://github.com/GavinPHR/Space-Time-AStar.git)
Copyright (c) 2020 [Haoran Peng]
Copyright (c) 2025 [Pengyuan Wei]
Released under the MIT License
'''
import numpy as np

class NeighbourTable3D:
    # 定义27个方向（包括当前点、6个面邻接点、12个边邻接点、8个角邻接点）
    directions = [
        (dx, dy, dz)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        for dz in [-1, 0, 1]
    ]

    def __init__(self, grid: np.ndarray):
        dimx, dimy, dimz, _ = grid.shape
        table = dict()
        for i in range(dimx):
            for j in range(dimy):
                for k in range(dimz):
                    neighbours = []
                    for dx, dy, dz in self.directions:
                        x, y, z = i + dx, j + dy, k + dz
                        if 0 <= x < dimx and 0 <= y < dimy and 0 <= z < dimz:
                            neighbours.append(grid[x][y][z])
                    table[self.hash(grid[i][j][k])] = np.array(neighbours)
        self.table = table

    def lookup(self, position: np.ndarray) -> np.ndarray:
        return self.table[self.hash(position)]

    @staticmethod
    def hash(grid_pos: np.ndarray) -> int:
        return tuple(grid_pos)

if __name__ == '__main__':
    grid = np.array([
        [
            [[15,5,0],[15,6,0],[15,7,0],[15,8,0],[15,9,0]],
            [[16,5,0],[16,6,0],[16,7,0],[16,8,0],[16,9,0]],
            [[17,5,0],[17,6,0],[17,7,0],[17,8,0],[17,9,0]],
            [[18,5,0],[18,6,0],[18,7,0],[18,8,0],[18,9,0]],
            [[19,5,0],[19,6,0],[19,7,0],[19,8,0],[19,9,0]]            
        ],
        [
            [[15,5,1],[15,6,1],[15,7,1],[15,8,1],[15,9,1]],
            [[16,5,1],[16,6,1],[16,7,1],[16,8,1],[16,9,1]],
            [[17,5,1],[17,6,1],[17,7,1],[17,8,1],[17,9,1]],
            [[18,5,1],[18,6,1],[18,7,1],[18,8,1],[18,9,1]],
            [[19,5,1],[19,6,1],[19,7,1],[19,8,1],[19,9,1]]   
        ],
        [
            [[15,5,2],[15,6,2],[15,7,2],[15,8,2],[15,9,2]],
            [[16,5,2],[16,6,2],[16,7,2],[16,8,2],[16,9,2]],
            [[17,5,2],[17,6,2],[17,7,2],[17,8,2],[17,9,2]],
            [[18,5,2],[18,6,2],[18,7,2],[18,8,2],[18,9,2]],
            [[19,5,2],[19,6,2],[19,7,2],[19,8,2],[19,9,2]]   
        ]
    ])
    nt = NeighbourTable3D(grid)
    print(nt.lookup(np.array([16,7,1])))