import pygame as pg
from game.game import Game
from game.menu import StartMenu, GameMenu, DeathMenu, WinMenu


def main():

    running = True

    pg.init()
    pg.mixer.init()
    pg.display.set_caption('Dodge the game')
    screen = pg.display.set_mode((600,600))
    clock = pg.time.Clock()

    # implement menus
    start_menu = StartMenu(screen, clock)
    game_menu = GameMenu(screen, clock)
    death_menu = DeathMenu(screen, clock)
    win_menu = WinMenu(screen, clock)

    # implement game
    game = Game(screen, clock)


    while running:
        pg.mixer.pause()
        # start menu goes here
        playing = start_menu.run()
        # bandera que nos ayuda a poner los objetos en su sitio desde un inicio
        flag = False
        music_flag = False
        current_time = 0
        pause_time = 0
        tries = 0

        while playing:

            total_time = int(pg.time.get_ticks()/1000)

            # game loop here
            game_state, current_time, music_flag = game.run(total_time, pause_time, flag, music_flag, tries)
            if game_state == 1:
                tries = 0
                playing = win_menu.run()
                #reiniciamos la musica
                pg.mixer.pause()
                music_flag = False
                #queremos que todo se coloque desde el principio
                flag = False
            elif game_state == 2:
                tries += 1
                playing = death_menu.run(total_time)
                #queremos que todo se coloque desde el principio
                flag = False
            elif game_state == 3:
                playing = game_menu.run()
                pause_time = current_time
                #queremos que no se muevan las posiciones de el jugador, enemigos etc
                flag = True


if __name__ == "__main__":
    main()