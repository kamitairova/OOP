import pygame

class Button:
    def __init__(self, rect: pygame.Rect, label: str, font: pygame.font.Font,
                 bg, bg_hover, fg, border=None, radius: int = 10):
        self.rect = rect
        self.label = label
        self.font = font
        self.bg = bg
        self.bg_hover = bg_hover
        self.fg = fg
        self.border = border
        self.radius = radius

    def is_hovered(self, mouse_pos) -> bool:
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen: pygame.Surface, mouse_pos):
        hovered = self.is_hovered(mouse_pos)
        color = self.bg_hover if hovered else self.bg

        pygame.draw.rect(screen, color, self.rect, border_radius=self.radius)
        if self.border is not None:
            pygame.draw.rect(screen, self.border, self.rect, width=2, border_radius=self.radius)

        text_surf = self.font.render(self.label, True, self.fg)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
