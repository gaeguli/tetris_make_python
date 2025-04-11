# map_arr =[
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],]
current_arr =[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],]
import keyword
import os
import time
import random as ran
import asyncio

async def console_clear():
    os.system('cls')

async def print_console(arr):
    """
    콘솔창 새로고침해주는 함수
    반드시 time.sleep()이랑 사용
    :param arr: 배열 (10 X 20)
    """
    await console_clear()
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 1:
                print("▣", end="")
            elif arr[i][j] == 2:
                print("□", end="")
            else:
                print(" ", end="")
        print()


async def find_block(arr):
    block_list = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 2:
                block_list.append([i, j])
    return block_list

async def move_block(arr, block):
    while True:
        can_move = True
        for x, y in block:
            new_x = x + 1
            if new_x >= len(arr) or arr[new_x][y] == (1 or 2):
                can_move = False
                break

        if not can_move:
            for x, y in block:
                arr[x][y] = 1
            break

        for x, y in block:
            arr[x][y] = 0
        block = [[x + 1, y] for x, y in block]
        for x, y in block:
            arr[x][y] = 2

        await print_console(arr)
        time.sleep(0.5)


async def make_block(arr):
    """
    새로운 블럭 만들어주는 함수
    """
    n = ran.randint(1, 7)
    if n == 1:
        block = [[1,4], [1,5], [1,6], [2,5]]
        await move_block(arr, block)
        return arr
    if n == 2:
        block = [[1, 4], [1, 5], [1, 6], [1, 7]]
        await move_block(arr, block)
        return arr


    return arr

async def control_block(arr):
    while True:
        if keyword.iskeyword("lift"):
            moveing_black = find_block(arr)
            for x, y in moveing_black:
                arr[x][y] = arr[x-1][y]


async def main():
    while True:
        await control_block(current_arr)
        current_arr = await make_block(current_arr)
        await print_console(current_arr)
        print(find_block(current_arr))
        time.sleep(1)


# while True:
    # asyncio.run(control_block(current_arr))
    # control_block(current_arr)
    # current_arr = make_block(current_arr)
    # print_console(current_arr)
    # print(find_block(current_arr))
    # time.sleep(1)

asyncio.run(main())