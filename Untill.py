# modules
import pygame
import random
import math

# init pygame
pygame.init()


class DrawInformation:
    # color declaration
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0 ,0
    BLUE = 0, 0, 255
    BACKGROUND_COLOR = WHITE
    
    GRADIENTS = [
        (128, 128, 128), 
        (160, 160, 160), 
        (192, 192, 192)
    ]

    # global non chaning vars
    FONT = pygame.font.SysFont('monospace', 30)
    LARGE_FONT = pygame.font.SysFont('monospace', 45)
    SIDE_PAD = 200
    TOP_PAD = 150

    # initializes vals
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    # self vals
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) /len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

# draw method
def draw(draw_info, algo_name, ascending):  
    # resets background
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # prints all titles
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 50))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 80))
    
    sorting = draw_info.FONT.render("M - Merge Sort | Q - Quick Sort | C - Change Size", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 110))


    # updates image with blits
    draw_list(draw_info)
    pygame.display.update()

# draws the list on the bottom of the page
def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    #  grid of rectangelar list
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                        draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    # tuple traversal
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        # greyscale coloration for visual difference
        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    # updated display as needed
    if clear_bg:
        pygame.display.update()

def list_update(draw_info, arr):
    pass

# generates a random starting image
def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    
    return lst

# prints all items in the array
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


