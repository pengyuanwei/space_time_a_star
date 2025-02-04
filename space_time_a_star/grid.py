#!/usr/bin/env python3
'''
Modified based on [Space-Time-AStar](https://github.com/GavinPHR/Space-Time-AStar.git)
Copyright (c) 2020 [Haoran Peng]
Copyright (c) 2025 [Pengyuan Wei]
Released under the MIT License
'''
from typing import Tuple
import numpy as np

class Grid:
    def __init__(self, 
                 grid_size: int, 
                 static_obstacles: np.array, 
                 three_dimensional: bool=False):
        
        self.grid_size = grid_size
        # The first obstacle is the boundary of the map.
        if not three_dimensional:
            self.minx, self.maxx, self.miny, self.maxy = self.calculate_boundaries(static_obstacles)
            self.grid = self.make_grid(grid_size, self.minx, self.maxx, self.miny, self.maxy)
        else:
            self.minx, self.maxx, self.miny, self.maxy, self.minz, self.maxz = self.calculate_boundaries_3d(static_obstacles)
            self.grid = self.make_3d_grid(grid_size, self.minx, self.maxx, self.miny, self.maxy, self.minz, self.maxz)

    @staticmethod
    def calculate_boundaries(static_obstacles: np.ndarray) -> Tuple[int, int, int, int]:
        min_ = np.min(static_obstacles, axis=0)
        max_ = np.max(static_obstacles, axis=0)
        return min_[0], max_[0], min_[1], max_[1]

    @staticmethod
    def calculate_boundaries_3d(static_obstacles: np.ndarray) -> Tuple[int, int, int, int, int, int]:
        min_ = np.min(static_obstacles, axis=0)
        max_ = np.max(static_obstacles, axis=0)
        return min_[0], max_[0], min_[1], max_[1], min_[2], max_[2]
    
    @staticmethod
    def make_grid(grid_size: int, minx: int, maxx: int, miny: int, maxy: int) -> np.ndarray:
        # Calculate the size of the sides
        x_size = (maxx - minx) // grid_size
        y_size = (maxy - miny) // grid_size
        # Initialize the grid, assuming grid is 2D
        grid = np.zeros([y_size, x_size, 2], dtype=np.int32)
        # Fill the grid in
        y = miny - grid_size / 2
        for i in range(y_size):
            y += grid_size
            x = minx - grid_size / 2
            for j in range(x_size):
                x += grid_size
                grid[i][j] = np.array([x, y])
        return grid

    # @staticmethod
    # def make_2d_grid(grid_size: int, minx: int, maxx: int, miny: int, maxy: int) -> np.ndarray:
    #     # 生成网格中心坐标
    #     x = np.arange(minx + grid_size / 2, maxx, grid_size)
    #     y = np.arange(miny + grid_size / 2, maxy, grid_size)

    #     # 使用 meshgrid 生成网格
    #     xx, yy = np.meshgrid(x, y, indexing='ij')

    #     # 组合成 [x, y] 坐标
    #     grid = np.stack([xx, yy], axis=-1)
    #     return grid
    
    @staticmethod
    def make_3d_grid(grid_size: int, minx: int, maxx: int, miny: int, maxy: int, minz: int, maxz: int) -> np.ndarray:
        # 生成网格中心坐标
        x = np.arange(minx + grid_size / 2, maxx, grid_size, dtype=np.int32)
        y = np.arange(miny + grid_size / 2, maxy, grid_size, dtype=np.int32)
        z = np.arange(minz + grid_size / 2, maxz, grid_size, dtype=np.int32)

        # 使用 meshgrid 生成三维网格
        xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')

        # 组合成 [x, y, z] 坐标
        grid = np.stack([xx, yy, zz], axis=-1)
        return grid

    '''
    Snap an arbitrary position to the center of the grid
    '''
    def snap_to_grid(self, position: np.ndarray) -> np.ndarray:
        i = (position[1] - self.miny) // self.grid_size
        j = (position[0] - self.minx) // self.grid_size
        if i >= len(self.grid):
            i -= 1
        if j >= len(self.grid[0]):
            j -= 1
        return self.grid[i][j]
    
    def snap_to_3d_grid(self, position: np.ndarray) -> np.ndarray:
        i = (position[0] - self.minx) // self.grid_size
        j = (position[1] - self.miny) // self.grid_size
        k = (position[2] - self.minz) // self.grid_size
        if i >= len(self.grid[0]):
            i -= 1
        if j >= len(self.grid[1]):
            j -= 1
        if k >= len(self.grid[2]):
            k -= 1
        return self.grid[i][j][k]