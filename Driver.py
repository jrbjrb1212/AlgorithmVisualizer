from Sorting_Algs import *

import sys

def get_text_input(screen, clock):
    pygame.init()
    user_text = ''
    FONT = pygame.font.SysFont('monospace', 30)
    text_surface = FONT.render(user_text, True, (255,255,255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.ext()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    print("HHHHH")
                    sys.ext()
                else:
                    user_text += event.unicode
        
        screen.window.fill(screen.BLACK)
        text_surface = FONT.render(user_text, True, (255,255,255))
        screen.window.blit(text_surface, (0,0))

        pygame.display.flip()
        clock.tick(60)



def main():
    run = True
    clock = pygame.time.Clock()

    n = 10
    min_val = 0
    max_val = 100
    sorting = False
    ascending = True


    lst = generate_starting_list(n, min_val, max_val)
    while True:
        raw_info = DrawInformation(800, 600, lst)
        get_text_input(raw_info, clock)

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None


    while run:
        clock.tick(10)

        if sorting:
            try:
                # print(sorting_algorithm_generator)
                # print(next(sorting_algorithm_generator))
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
    
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            
            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"

            

            
    pygame.quit()

if __name__ == "__main__":
    main()