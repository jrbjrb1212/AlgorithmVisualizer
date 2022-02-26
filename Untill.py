import pygame
import random
import math

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0 ,0
    BACKGROUND_COLOR = WHITE
    
    GRADIENTS = [
        (128, 128, 128), 
        (160, 160, 160), 
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('monospace', 20)
    LARGE_FONT = pygame.font.SysFont('monospace', 35)
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) /len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending, backOnly):
    if backOnly:
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    else:
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)
        

        title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
        draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

        controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
        draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 50))

        sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.BLACK)
        draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 80))

        draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                        draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    
    return lst


# def bubble_sort(draw_info, ascending = True):
#     lst = draw_info.lst

#     for i in range(len(lst) - 1):
#         for j in range(len(lst) - 1 - i):
#             num1 = lst[j]
#             num2 = lst[j+1]


#             if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
#                 # quick way to swap with using temp variable
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#                 draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)

#                 # avoids only running this method at a time
#                 yield True
#     return lst

# def insertion_sort(draw_info, ascending=True):
#     lst = draw_info.lst

#     for i in range(1, len(lst)):
#         current = lst[i]

#         while True:
#             ascending_sort = i > 0 and lst[i-1] > current and ascending
#             descending_sort = i > 0 and lst[i-1] > current and not ascending

#             if not ascending_sort and not descending_sort:
#                 break

#             lst[i] = lst[i-1]
#             i = i - 1
#             lst[i] = current
#             draw_list(draw_info, {i-1: draw_info.GREEN, i: draw_info.RED}, True)
#             yield True
    
#     return lst


# # def merge_intro(draw_info, ascending=True):
# #     lst = draw_info.lst
# #     print(lst)
# #     lst = mergeSort(lst)
# #     return lst

# def selection_sort(draw_info, ascending=True):
#     lst = draw_info.lst
#     i = 0
#     j = len(lst) - 1
#     print(ascending)
#     while i < j:
#         min_idx = i
#         max_idx = i
#         max_val = lst[i]
#         if ascending:
#             for k in range(i, j+1):
#                 if lst[min_idx] > lst[k]:
#                     min_idx = k
#                 if lst[max_idx] < lst[k] and ascending:
#                     max_idx = k
#                     max_val = lst[k]
#                     draw_list(draw_info, {max_idx: draw_info.GREEN, k: draw_info.RED}, True)


#             lst[i], lst[min_idx] = lst[min_idx], lst[i]
#             draw_list(draw_info, {min_idx: draw_info.GREEN, i: draw_info.RED}, True)


#             # Edge-case: if we shifted the value to the maximum in the last swap
#             if lst[min_idx] == max_val and ascending:
#                 lst[j], lst[min_idx] = lst[min_idx], lst[j]
#                 draw_list(draw_info, {min_idx: draw_info.GREEN, j: draw_info.RED}, True)
#                 yield True
#             elif lst[min_idx] != max_val and ascending:
#                 lst[j], lst[max_idx] = lst[max_idx], lst[j]
#                 draw_list(draw_info, {max_idx: draw_info.GREEN, j: draw_info.RED}, True)
#                 yield True

#             i += 1
#             j -= 1

#         else:
#             for k in range(i, j+1):
#                 if lst[max_idx] < lst[k]:
#                     max_idx = k
#                     max_val = lst[k]
#                     draw_list(draw_info, {max: draw_info.GREEN, k: draw_info.RED}, True)
#                 if lst[min_idx] > lst[k]:
#                     min_idx = k
#                     min_idx = lst[k]
#                     draw_list(draw_info, {min_idx: draw_info.GREEN, k: draw_info.RED}, True)


#             lst[i], lst[min_idx] = lst[min_idx], lst[i]
#             draw_list(draw_info, {min_idx: draw_info.GREEN, i: draw_info.RED}, True)
#             yield True


#             # Edge-case: if we shifted the value to the maximum in the last swap
#             if lst[min_idx] == max_val:
#                 lst[j], lst[min_idx] = lst[min_idx], lst[j]
#                 draw_list(draw_info, {min_idx: draw_info.GREEN, j: draw_info.RED}, True)
#                 yield True
#             elif lst[min_idx] != max_val:
#                 lst[j], lst[max_idx] = lst[max_idx], lst[j]
#                 draw_list(draw_info, {max_idx: draw_info.GREEN, j: draw_info.RED}, True)
#                 yield True
            
#             i += 1
#             j -= 1

#     return lst



def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


