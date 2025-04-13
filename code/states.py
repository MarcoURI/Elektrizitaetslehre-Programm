# state

class State():
    def __init__(self,menu):
        self.menu = menu
        self.prev_state = None

    def update(self,delta_time, actions):
        pass
    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.state_stack) > 1:
            self.prev_state = self.menu.state_staxk[-1]
        self.menu.state_stack.append(self)

    def exit_state(self):
        self.menu.stack.pop()