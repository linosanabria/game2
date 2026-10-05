import pygame

class AssetManager:
    """Gerenciador centralizado de recursos com suporte a cache."""
    _fonts = {}

    @classmethod
    def get_font(cls, name: str, size: int) -> pygame.font.Font:
        key = (name, size)
        if key not in cls._fonts:
            cls._fonts[key] = pygame.font.SysFont(name, size)
        return cls._fonts[key]
