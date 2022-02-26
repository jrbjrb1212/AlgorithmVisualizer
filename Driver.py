from Sorting_Algs import *

import sys
import pygame

def get_text_input(screen, clock):
    user_text = ''
    small_font = pygame.font.SysFont('monospace', 25)
    font = pygame.font.SysFont('monospace', 30)
    text_surface = font.render(user_text, True, (255,255,255))
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                elif event.key == pygame.K_RETURN and len(user_text) > 0:
                    run = False

                else:
                    user_text += event.unicode
        
        screen.window.fill(screen.BLACK)
        text_surface = font.render(user_text, True, (255,255,255))
        screen.window.blit(text_surface, (400,300))
        controls = small_font.render("Enter the amount of element you would like to sort:", 1, screen.WHITE)
        screen.window.blit(controls, (screen.width/2 - controls.get_width()/2, 250))

        pygame.display.flip()
        clock.tick()
    
    screen.window.fill(screen.BLACK)
    speed = -5
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.ext()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    # slow speed
                    speed = 10
                    run = False

                elif event.key == pygame.K_a:
                    # average speed
                   speed = 60
                   run = False

                elif event.key == pygame.K_f:
                    # fast speed
                    speed = 120
                    run = False

                elif event.key == pygame.K_v:
                    # very fast speed
                    speed = 0
                    run = False
                    
        
        screen.window.fill(screen.BLACK)
        controls = small_font.render("Sorting Speed:", 1, screen.WHITE)
        speeeds = small_font.render("Slow(S)     Average(A)    Fast(F)     Very Fast(V)", 1, screen.WHITE)
        screen.window.blit(controls, (screen.width/2 - controls.get_width()/2, 200))
        screen.window.blit(speeeds, (screen.width/2 - speeeds.get_width()/2, 250))

        pygame.display.flip()
        clock.tick()
    
    return user_text, speed


def main():
    run = True
    clock = pygame.time.Clock()

    
    n = 10
    min_val = 0
    max_val = 100
    sorting = False
    ascending = True


    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    n, speed = get_text_input(draw_info, clock)
    n = int(n)
    speed = int(speed)

    lst = generate_starting_list(n, min_val, max_val)
    draw_info.set_list(lst)

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None


    while run:
        if speed == 0:
            clock.tick()
        else:
            clock.tick(speed)

        if sorting:
            try:
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

            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_intro
                sorting_algo_name = "Merge Sort"
            
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort_intro
                sorting_algo_name = "Quick Sort"

                 
    pygame.quit()

if __name__ == "__main__":
    main()