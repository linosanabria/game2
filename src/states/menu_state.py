import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_NEON_PINK, COLOR_NEON_CYAN, COLOR_WHITE
from src.states.base_state import BaseState
from src.core.asset_manager import AssetManager

class MenuState(BaseState):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.manager.change_state("play")

    def draw(self, surface):
        surface.fill((15, 10, 30))
        font_title = AssetManager.get_font("Arial", 48)
        font_sub = AssetManager.get_font("Arial", 24)

        title_surf = font_title.render("CYBER RUN", True, COLOR_NEON_PINK)
        sub_surf = font_sub.render("Pressione ESPAÇO para Iniciar", True, COLOR_NEON_CYAN)

        surface.blit(title_surf, title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)))
        surface.blit(sub_surf, sub_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)))
