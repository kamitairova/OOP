import pygame
from model import Calculator
from view import CalculatorView

class CalculatorController:
    """
    Controller: handles events and connects Model <-> View
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MVC Calculator (Pygame)")
        self.clock = pygame.time.Clock()

        self.view = CalculatorView()
        self.screen = pygame.display.set_mode((self.view.width, self.view.height))

        self.model = Calculator()
        self.result_hint = None
        self.running = True

        # Map UI labels to model actions
        self.char_buttons = set("0123456789.+-*/()")

    def _apply_action(self, label: str):
        self.result_hint = None

        if label == "C":
            self.model.clear_expression()
            return

        if label == "卐":
            self.model.remove_last_character()
            return

        if label == "=":
            res = self.model.calculate()
            if isinstance(res, (int, float)):
                self.model.expression = str(res)
            else:
                # error string
                self.result_hint = res
            return

        if label in self.char_buttons:
            # Small guard: avoid two operators in a row (optional UX)
            if label in "+-*/":
                if self.model.expression == "":
                    if label == "-":  # allow negative numbers
                        self.model.add_to_expression(label)
                    return
                if self.model.expression[-1] in "+-*/":
                    self.model.remove_last_character()
            self.model.add_to_expression(label)

    def _handle_mouse(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for label, btn in self.view.buttons.items():
                if btn.rect.collidepoint(mouse_pos):
                    self._apply_action(label)
                    break

    def _handle_keyboard(self, event: pygame.event.Event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_ESCAPE:
            self.running = False
            return

        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            self._apply_action("=")
            return

        if event.key == pygame.K_BACKSPACE:
            self._apply_action("⌫")
            return

        if event.key == pygame.K_DELETE:
            self._apply_action("C")
            return

        # Accept digits/operators/parentheses/dot
        ch = event.unicode
        if ch and ch in self.char_buttons:
            self._apply_action(ch)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                self._handle_mouse(event)
                self._handle_keyboard(event)

            mouse_pos = pygame.mouse.get_pos()
            self.view.draw(self.screen, self.model.get_expression(), self.result_hint, mouse_pos)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
