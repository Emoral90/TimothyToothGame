

import pygame
import pygame_gui


def init_game():
    '''
    A function to initialize a blank pygame window
    '''

    pygame.init()

    pygame.display.set_caption("Quick Start")
    window_surface = pygame.display.set_mode((1000, 720))

    background = pygame.Surface((1000, 720))
    background.fill(pygame.Color("#dfdfdf"))

    # A manager to handle calling the update, draw, and event handling functions of all UI elements
    manager = pygame_gui.UIManager((1000, 720))

    # Create a UIButton in the middle of the window and prints "Hello World"
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((436, 296),
                                                                            (64, 64)),
                                                                            text="Say Hello",
                                                                            manager=manager)

    # Create a clock to track the amount of seconds that elapse between each while loop
    clock = pygame.time.Clock()
    is_running = True

    # MAIN GAME LOOP
    while is_running:
        # Fix the framerate of the program, so as to not strain your computer
        # Otherwise, it will execute as fast as possible
        time_delta = clock.tick(60)/1000
        for event in pygame.event.get():
            # Establish what happens if user exits/closes window
            if event.type == pygame.QUIT:
                is_running = False

            # Make it so if any UIButton, specifically if the hello_button is pressed, then print "Hello World" to the console
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print("Hello World")

            manager.process_events(event)
        manager.update(time_delta)

        window_surface.blit(background, (0,0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def main():
    init_game()

if __name__ == "__main__":
    main()