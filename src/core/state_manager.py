class StateManager:
    """Gerencia a transição e atualização de telas (State Pattern)."""
    def __init__(self):
        self._states = {}
        self._current_state = None

    def add_state(self, name: str, state_instance):
        self._states[name] = state_instance

    def change_state(self, name: str):
        if name in self._states:
            self._current_state = self._states[name]
            if hasattr(self._current_state, "enter"):
                self._current_state.enter()

    def handle_events(self, events):
        if self._current_state:
            self._current_state.handle_events(events)

    def update(self, dt: float):
        if self._current_state:
            self._current_state.update(dt)

    def draw(self, surface):
        if self._current_state:
            self._current_state.draw(surface)
