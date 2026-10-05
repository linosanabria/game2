import sys
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from src.core.state_manager import StateManager
from src.states.menu_state import MenuState
from src.states.play_state import PlayState

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    state_manager = StateManager()
    state_manager.add_state("menu", MenuState(state_manager))
    state_manager.add_state("play", PlayState(state_manager))
    state_manager.change_state("menu")

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        state_manager.handle_events(events)
        state_manager.update(dt)
        state_manager.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
