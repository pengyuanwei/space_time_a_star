#!/usr/bin/env python3
'''
Modified based on [Space-Time-AStar](https://github.com/GavinPHR/Space-Time-AStar.git)
Copyright (c) 2020 [Haoran Peng]
Copyright (c) 2025 [Pengyuan Wei]
Released under the MIT License
'''
import numpy as np

class State:
    def __init__(self, pos: np.ndarray, time: int, g_score: int, h_score: int):
        self.pos = pos          # 当前状态的位置坐标（通常是二维数组，如 [x, y]）
        self.time = time        # 当前状态的时间步
        self.g_score = g_score  # 从起点到当前状态的实际代价
        self.f_score = g_score + h_score  # A*的总评估值 f = g + h（h是启发式估计值）

    # 在哈希表（如集合或字典）中唯一标识一个状态，可用于判断状态是否已存在于 closed_list
    def __hash__(self) -> int:
        if len(self.pos) == 2:
            concat = str(self.pos[0]) + str(self.pos[1]) + '0' + str(self.time)
        elif len(self.pos) == 3:
            concat = str(self.pos[0]) + str(self.pos[1]) + str(self.pos[2]) + '0' + str(self.time)
        else:
            print("Wrong dimension of location!")        
        return int(concat)

    # 判断是否到达目标位置，忽略时间因素
    def pos_equal_to(self, pos: np.ndarray) -> bool:
        return np.array_equal(self.pos, pos)

    # 小于运算符重载：基于 f_score 判断优先级
    def __lt__(self, other: 'State') -> bool:
        return self.f_score < other.f_score

    # 相等运算符重载：通过比较哈希值判断两个状态是否相等
    def __eq__(self, other: 'State') -> bool:
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return 'State(pos=[' + str(self.pos[0]) + ', ' + str(self.pos[1]) + '], ' \
               + 'time=' + str(self.time) + ', fscore=' + str(self.f_score) + ')'

    # print(state) 时显示位置、时间和 f_score
    def __repr__(self):
        return self.__str__()
