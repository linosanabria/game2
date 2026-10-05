class BaseState:
    """Classe base abstrata para todos os estados do jogo."""
    def __init__(self, manager):
        self.manager = manager

    def handle_events(self, events): pass
    def update(self, dt: float): pass
    def draw(self, surface): pass
    def enter(self): pass
