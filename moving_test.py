import time

import keyboard
import os

current_arr =[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],]

def control_block(arr):
    while True:
        if keyboard.is_pressed('left'):
            block = find_block(arr)

            # 블럭이 왼쪽으로 이동 가능한지 확인
            can_move = all(y >= 1 and arr[x][y-1] == 0 for x, y in block)

            if can_move:
                # 기존 블록 지우기
                for x, y in block:
                    arr[x][y] = 0

                # 왼쪽으로 이동
                new_block = [[x, y - 1] for x, y in block]
                for x, y in new_block:
                    arr[x][y] = 2

                print_console(arr)
            time.sleep(0.1)

        if keyboard.is_pressed('right'):
            block = find_block(arr)

            # 블럭이 오른쪽으로 이동 가능한지 확인
            can_move = all(y >= 1 and arr[x][y+1] == 0 for x, y in block)

            if can_move:
                # 기존 블록 지우기
                for x, y in block:
                    arr[x][y] = 0

                # 왼쪽으로 이동
                new_block = [[x, y + 1] for x, y in block]
                for x, y in new_block:
                    arr[x][y] = 2

                print_console(arr)
            time.sleep(0.1)



def find_block(arr):
    block_list = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 2:
                block_list.append([i, j])
    return block_list

def console_clear():
    os.system('cls')

def print_console(arr):
    """
    콘솔창 새로고침해주는 함수
    반드시 time.sleep()이랑 사용
    :param arr: 배열 (10 X 20)
    """
    console_clear()
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 1:
                print("▣", end="")
            elif arr[i][j] == 2:
                print("□", end="")
            else:
                print(" ", end="")
        print()


while True:
    control_block(current_arr)