# inheritances that is not inheritances
from Sorting_Algs import *

# modules
import sys
import pygame

# input text 
def get_text_input(screen, clock):
    user_text = ''
    # different fonts
    small_font = pygame.font.SysFont('monospace',35, bold=True, )
    font = pygame.font.SysFont('monospace', 45,  bold=True)
    large_font = pygame.font.SysFont('monospace', 75,  bold=True)
    text_surface = font.render(user_text, True, (255,255,255))
    run = True

    # runs untill an enter
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
        text_surface = large_font.render(user_text, True, (255,255,255))
        controls = small_font.render("Enter the amount of element you would like to sort:", 1, screen.WHITE)
        screen.window.blit(text_surface, (screen.width/2 - controls.get_width()/2 + 450,300))
        screen.window.blit(controls, (screen.width/2 - controls.get_width()/2, 250))

        pygame.display.flip()
        clock.tick()
    
    screen.window.fill(screen.BLACK)
    speed = -5
    run = True

    # speed
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
        controls = font.render("Sorting Speed:", 1, screen.WHITE)
        speeeds = font.render("Slow(S)     Average(A)    Fast(F)     Very Fast(V)", 1, screen.WHITE)
        screen.window.blit(controls, (screen.width/2 - controls.get_width()/2, 200))
        screen.window.blit(speeeds, (screen.width/2 - speeeds.get_width()/2, 300))

        pygame.display.flip()
    
    return user_text, speed


def main():
    run = True
    clock = pygame.time.Clock()

    
    n = 10
    min_val = 10
    max_val = 100
    sorting = False
    ascending = True


    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1500, 800, lst)
    n, speed = get_text_input(draw_info, clock)
    n = int(n)
    speed = int(speed)

    lst = generate_starting_list(n, min_val, max_val)
    draw_info.set_list(lst)

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    # run condition
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
            except TypeError:
                pygame.time.delay(3000)
                main()
        else:
            # redraw if not sorting
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
            
            # resets
            # genartes new list
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
    
            # starts sorting
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            
            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            # insertion
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            
            # bubble
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

            # selection
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"

            # merge
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_intro
                sorting_algo_name = "Merge Sort"
            
            #  quick
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort_intro
                sorting_algo_name = "Quick Sort"

            # rest
            elif event.key == pygame.K_c:
                main()

                 
    pygame.quit()

# start game
if __name__ == "__main__":
    main()