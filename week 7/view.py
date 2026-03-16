import pygame
from ui.button import Button

class CalculatorView:
    """
    View: draws UI and exposes button map.
    """
    def __init__(self, width: int = 420, height: int = 640):
        self.width = width
        self.height = height

        # Theme
        self.bg = (12, 16, 28)
        self.panel = (18, 24, 40)
        self.panel2 = (22, 30, 52)
        self.text = (236, 240, 255)
        self.muted = (160, 170, 200)
        self.accent = (98, 200, 165)
        self.danger = (255, 102, 120)

        self.display_rect = pygame.Rect(24, 24, self.width - 48, 110)
        self.pad_rect = pygame.Rect(24, 160, self.width - 48, self.height - 184)

        self.font_display = pygame.font.SysFont("consolas", 36, bold=True)
        self.font_small = pygame.font.SysFont("consolas", 18)
        self.font_btn = pygame.font.SysFont("consolas", 26, bold=True)

        self.buttons = {}  # label -> Button
        self._build_buttons()

    def _build_buttons(self):
        # Layout: 4 columns x 5 rows
        labels = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        gap = 12
        cols, rows = 4, 5
        x0, y0 = self.pad_rect.x, self.pad_rect.y
        w = (self.pad_rect.width - gap * (cols - 1)) // cols
        h = (self.pad_rect.height - gap * (rows - 1)) // rows

        for r in range(rows):
            for c in range(cols):
                label = labels[r][c]
                rect = pygame.Rect(x0 + c * (w + gap), y0 + r * (h + gap), w, h)

                if label in {"+", "-", "*", "/"}:
                    bg = (34, 44, 74)
                    bg_hover = (44, 56, 92)
                    fg = self.text
                    border = (70, 90, 140)
                elif label == "=":
                    bg = (40, 120, 95)
                    bg_hover = (55, 150, 118)
                    fg = (255, 255, 255)
                    border = None
                elif label == "C":
                    bg = (120, 45, 58)
                    bg_hover = (150, 60, 76)
                    fg = (255, 255, 255)
                    border = None
                else:
                    bg = (26, 34, 56)
                    bg_hover = (34, 44, 74)
                    fg = self.text
                    border = (52, 66, 110)

                self.buttons[label] = Button(rect, label, self.font_btn, bg, bg_hover, fg, border=border, radius=14)

    def draw(self, screen: pygame.Surface, expression: str, result_hint: str | None, mouse_pos):
        screen.fill(self.bg)

        # Display panel
        pygame.draw.rect(screen, self.panel, self.display_rect, border_radius=18)
        pygame.draw.rect(screen, self.panel2, self.display_rect, width=2, border_radius=18)

        # Expression text (right aligned)
        expr = expression if expression else "0"
        expr_surf = self.font_display.render(expr, True, self.text)
        expr_rect = expr_surf.get_rect()
        expr_rect.right = self.display_rect.right - 14
        expr_rect.centery = self.display_rect.centery - 10

        # Clip if too long
        clip_rect = self.display_rect.inflate(-20, -20)
        old_clip = screen.get_clip()
        screen.set_clip(clip_rect)
        screen.blit(expr_surf, expr_rect)
        screen.set_clip(old_clip)

        # Hint line
        hint = result_hint or "Click buttons or type on keyboard (Enter =, Backspace ⌫)"
        hint_surf = self.font_small.render(hint, True, self.muted)
        screen.blit(hint_surf, (self.display_rect.x + 14, self.display_rect.bottom - 28))

        # Buttons
        for btn in self.buttons.values():
            btn.draw(screen, mouse_pos)
