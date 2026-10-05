import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BG, COLOR_NEON_PINK, COLOR_NEON_YELLOW, GROUND_Y, INITIAL_SPEED, SPEED_INCREMENT
from src.states.base_state import BaseState
from src.entities.player import Player
from src.core.asset_manager import AssetManager

class PlayState(BaseState):
    def enter(self):
        self.player = Player(100, GROUND_Y)
        self.all_sprites = pygame.sprite.Group(self.player)
        self.score = 0.0
        self.speed = INITIAL_SPEED
        self.bg_offset = 0.0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    self.player.jump()

    def update(self, dt: float):
        self.speed += SPEED_INCREMENT
        self.score += self.speed * 0.1
        self.bg_offset = (self.bg_offset + self.speed * 0.5) % SCREEN_WIDTH
        self.all_sprites.update(dt)

    def draw(self, surface):
        surface.fill(COLOR_BG)

        # Fundo Parallax (Efeito Néon)
        for i in range(-1, 2):
            x_pos = i * SCREEN_WIDTH - int(self.bg_offset)
            pygame.draw.line(surface, (40, 20, 60), (x_pos, GROUND_Y - 100), (x_pos + SCREEN_WIDTH, GROUND_Y - 100), 2)

        # Chão cibernético
        pygame.draw.rect(surface, COLOR_NEON_PINK, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))

        # Sprites
        self.all_sprites.draw(surface)

        # HUD / Pontuação
        font = AssetManager.get_font("Arial", 20)
        score_surf = font.render(f"SCORE: {int(self.score)}", True, COLOR_NEON_YELLOW)
        surface.blit(score_surf, (20, 20))
