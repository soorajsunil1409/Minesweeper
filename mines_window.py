import pygame
import utils
import copy
from board_generator import generate_board, generate_neighbor_board

from pygame import gfxdraw

class Tile:
    def __init__(self, x, y, width, screen, mine: bool = False, value: int = 0):
        self.content = None
        self.closed = 1
        self.mine = mine
        self.value = str(value) if value not in (0, -1) else ""
        self.neighbor_mines = 0
        self.walls = [0, 0, 0, 0]   # left right top bottom
        self.line_width = 2
        self.x = x*width
        self.y = y*width+utils.TOP_BAR_HEIGHT
        self.row = x
        self.col = y
        self.width = width
        self.colors = None

        self.screen = screen

        self.font = pygame.font.SysFont("Helvetica", 18)

    def event_update(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if self.x < x < self.x+self.width and self.y < y < self.y+self.width:
                if self.closed:
                    self.closed = False
                    if not self.mine:
                        return "number" if self.value else "space"
                    else:
                        return "mine"
                else:
                    return "opened"


    def draw(self):
        color = self.colors[0] if self.closed else self.colors[1]

        box = pygame.draw.rect(self.screen, color, (self.x, self.y, self.width, self.width))

        self.mine_text = self.font.render(self.value, True, utils.BLACK)
        self.mine_text_rect = self.mine_text.get_rect()
        self.mine_text_rect.center = box.center

        if not self.closed:
            if self.mine:
                pygame.draw.circle(self.screen, (0, 0, 0), (self.x+self.width//2, self.y+self.width//2), self.width//4, 20)
                
            self.screen.blit(self.mine_text, self.mine_text_rect)

        if self.walls[0]: pygame.draw.line(self.screen, utils.TILE_BORDER_COLOR, (self.x, self.y), (self.x, self.y+self.width), self.line_width)
        if self.walls[1]: pygame.draw.line(self.screen, utils.TILE_BORDER_COLOR, (self.x+self.width, self.y), (self.x+self.width, self.y+self.width), self.line_width+4)
        if self.walls[2]: pygame.draw.line(self.screen, utils.TILE_BORDER_COLOR, (self.x, self.y), (self.x+self.width, self.y), self.line_width)
        if self.walls[3]: pygame.draw.line(self.screen, utils.TILE_BORDER_COLOR, (self.x, self.y+self.width), (self.x+self.width, self.y+self.width), self.line_width+4)


class MinesWindow:
    def __init__(self, screen):
        self.board = []
        self.size = None
        self.mines = None
        self.mines_idx = None
        self.screen = screen

        self.reinitialize_board(utils.Difficulty.EASY)

    def trigger_game_loss(self):
        for x, y in self.mines_idx:
            if self.board[y][x].closed:
                self.board[y][x].closed = False

    def reinitialize_board(self, diff: utils.Difficulty):
        self.size = utils.WINDOW_SIZES[diff.value]
        self.mines = utils.WINDOW_MINES_COUNT[diff.value]
        tile_width = utils.TILE_WIDTH[diff.value]

        self.board, self.mines_idx = generate_neighbor_board(self.size, self.mines)

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                mine = 1 if self.board[y][x] == -1 else 0
                value = self.board[y][x]
                self.board[y][x] = Tile(x, y, tile_width, self.screen, mine, value)
                self.board[y][x].colors = (utils.EVEN_TILE_COLOR_CLOSED, utils.EVEN_TILE_COLOR_OPEN) if (x+y) % 2 != 0 else (utils.ODD_TILE_COLOR_CLOSED, utils.ODD_TILE_COLOR_OPEN)


    def event_update(self, event):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                ev = self.board[y][x].event_update(event)
                if ev: print(ev)


    def draw(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.board[y][x].walls = [0, 0, 0, 0]
                if not self.board[y][x].closed:
                    if y-1 >= 0:
                        if self.board[y-1][x].closed: self.board[y][x].walls[2] = 1
                    if y+1 < self.size[1]:
                        if self.board[y+1][x].closed: self.board[y][x].walls[3] = 1
                    if x-1 >= 0:
                        if self.board[y][x-1].closed: self.board[y][x].walls[0] = 1
                    if x+1 < self.size[0]:
                        if self.board[y][x+1].closed: self.board[y][x].walls[1] = 1
                self.board[y][x].draw()