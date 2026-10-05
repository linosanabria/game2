import pygame
from config import GROUND_Y, GRAVITY, JUMP_FORCE, COLOR_NEON_CYAN

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(COLOR_NEON_CYAN)
        self.rect = self.image.get_rect(bottomleft=(x, y))
        
        self.velocity_y = 0.0
        self.is_grounded = True

    def jump(self):
        if self.is_grounded:
            self.velocity_y = JUMP_FORCE
            self.is_grounded = False

    def update(self, dt: float):
        # Aplicação de gravidade
        self.velocity_y += GRAVITY
        self.rect.y += int(self.velocity_y)

        # Colisão com o chão
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.velocity_y = 0.0
            self.is_grounded = True
