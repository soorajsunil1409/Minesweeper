import pygame
import utils

from pygame import gfxdraw

class TopBar:
    def __init__(self):
        self.current_sel = utils.Difficulty.EASY
        self.font = pygame.font.SysFont("Helvetica", 18)

        self.render_text()

    def render_text(self):
        self.easy_text = self.font.render("Easy", True, utils.BLACK, utils.BTN_COLOR)
        self.med_text = self.font.render("Medium", True, utils.BLACK, utils.BTN_COLOR)
        self.hard_text = self.font.render("Hard", True, utils.BLACK, utils.BTN_COLOR)

        self.easy_rect = pygame.Rect(utils.BTN_MARGIN, utils.BTN_MARGIN, utils.BTN_WIDTH, utils.BTN_HEIGHT)
        self.med_rect = pygame.Rect(2*utils.BTN_MARGIN + utils.BTN_WIDTH, utils.BTN_MARGIN, utils.BTN_WIDTH, utils.BTN_HEIGHT)
        self.hard_rect = pygame.Rect(3*utils.BTN_MARGIN + 2*utils.BTN_WIDTH, utils.BTN_MARGIN, utils.BTN_WIDTH, utils.BTN_HEIGHT)

        self.easy_text_rect = self.easy_text.get_rect()
        self.easy_text_rect.center = self.easy_rect.center
        self.med_text_rect = self.med_text.get_rect()
        self.med_text_rect.center = self.med_rect.center
        self.hard_text_rect = self.hard_text.get_rect()
        self.hard_text_rect.center = self.hard_rect.center

    def draw(self, screen: pygame.Surface, size):
        top_bar_rect = pygame.Rect(0, 0, size[0], utils.TOP_BAR_HEIGHT)
        pygame.draw.rect(screen, color=utils.TOP_BAR_COLOR, rect=top_bar_rect)

        self.easy_btn = pygame.draw.rect(screen, color=utils.BTN_COLOR, rect=self.easy_rect, border_radius=3)
        self.med_btn  = pygame.draw.rect(screen, color=utils.BTN_COLOR, rect=self.med_rect, border_radius=3)
        self.hard_btn = pygame.draw.rect(screen, color=utils.BTN_COLOR, rect=self.hard_rect, border_radius=3)

        screen.blit(self.easy_text, self.easy_text_rect)
        screen.blit(self.med_text, self.med_text_rect)
        screen.blit(self.hard_text, self.hard_text_rect)

    def event_update(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if self.easy_btn.left <= x <= self.easy_btn.right and self.easy_btn.top <= y <= self.easy_btn.bottom:
                # print("Easy button pressed")
                self.current_sel = utils.Difficulty.EASY

            if self.med_btn.left <= x <= self.med_btn.right and self.med_btn.top <= y <= self.med_btn.bottom:
                # print("Medium button pressed")
                self.current_sel = utils.Difficulty.MEDIUM

            if self.hard_btn.left <= x <= self.hard_btn.right and self.hard_btn.top <= y <= self.hard_btn.bottom:
                # print("Hard button pressed")
                self.current_sel = utils.Difficulty.HARD