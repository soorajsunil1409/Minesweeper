import pygame
import sys
import utils

from mines_window import MinesWindow
from top_bar import TopBar

pygame.init()
prev_screen_size = utils.Difficulty.EASY


def get_screen_surface(size) -> pygame.Surface:
    return pygame.display.set_mode(size)

def main():
    global prev_screen_size

    screen = get_screen_surface(utils.SCREEN_SIZE)

    topBar = TopBar()
    minesWindow = MinesWindow(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #region External Events

            topBar.event_update(event)
            minesWindow.event_update(event)

            #endregion

        if (topBar.current_sel == utils.Difficulty.EASY and prev_screen_size != utils.WINDOW_SIZE_E):
            screen = get_screen_surface(utils.WINDOW_SIZE_E)
            prev_screen_size = utils.WINDOW_SIZE_E
            minesWindow.reinitialize_board(topBar.current_sel)
        elif (topBar.current_sel == utils.Difficulty.MEDIUM and prev_screen_size != utils.WINDOW_SIZE_M):
            screen = get_screen_surface(utils.WINDOW_SIZE_M)
            prev_screen_size = utils.WINDOW_SIZE_M
            minesWindow.reinitialize_board(topBar.current_sel)
        elif (topBar.current_sel == utils.Difficulty.HARD and prev_screen_size != utils.WINDOW_SIZE_H):
            screen = get_screen_surface(utils.WINDOW_SIZE_H)
            prev_screen_size = utils.WINDOW_SIZE_H
            minesWindow.reinitialize_board(topBar.current_sel)

        screen.fill(utils.BG_COLOR)

        #region UPDATE

        topBar.draw(screen, prev_screen_size)
        minesWindow.draw()

        #endregion

        pygame.display.flip()

if __name__ == "__main__":
    main()