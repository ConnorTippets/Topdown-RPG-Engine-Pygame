import pygame, sys
from properties import *
from player import *
from map import *
screen = pygame.display.set_mode(wSize, pygame.RESIZABLE)
pygame.display.set_caption('Pygame Basis for a topdown RPG-like game engine made by GITHUB-ConnorTippets')
clock = pygame.time.Clock()
#Initialize the window with a caption explaining the game
#And create a clock for keeping at the target fps (properties.tFPS)

def draw_map():
    for y in range(mRows):
        for x in range(mCols):
            xy = map.map[y*mRows+x]
            if xy > 0:
                pygame.draw.rect(screen, tColor, map.collision[y*mRows+x])

def draw_player():
    #Create a rectangle the size of the player (player.w, player.h), centered at the players x and y (player.x and player.y)
    #And draw it to the screen with a red color
    pygame.draw.rect(screen, (255,0,0), player.update_rectangle())

def handle_controls(keys, shift=False):
    #When no arrow keys are held, this is 0, which doesn't move at all
    #When the left arrow key is held, this is -1, which counts as moving left by 10 pixels
    #When the right arrow key is held, this is 1, which counts as moving right by 10 pixels
    #When both arrow keys are held, this is 0, which doesn't move at all
    player.handle_controls_x(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], (True if shift else False))
    _ = player.update_rectangle()
    if map.collide(_):
        #If the player is colliding with the map, slowly move the opposite direction until not colliding
        #Also check for running to change accordingly
        while map.collide(_):
            player.handle_controls_x(((-0.05 if not (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) < 0 else 0.05) if shift else (-0.1 if not (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) < 0 else 0.1)), (True if shift else False))
            _ = player.update_rectangle()
    #When no arrow keys are held, this is 0, which doesn't move at all
    #When the down arrow key is held, this is -1, which counts as moving down by 10 pixels
    #When the up arrow key is held, this is 1, which counts as moving up by 10 pixels
    #When both arrow keys are held, this is 0, which doesn't move at all
    player.handle_controls_y(keys[pygame.K_UP] - keys[pygame.K_DOWN], (True if shift else False))
    _ = player.update_rectangle()
    if map.collide(_):
        #If the player is colliding with the map, slowly move the opposite direction until not colliding
        while map.collide(_):
            player.handle_controls_y(((-0.05 if not (keys[pygame.K_UP] - keys[pygame.K_DOWN]) < 0 else 0.05) if shift else (-0.1 if not (keys[pygame.K_UP] - keys[pygame.K_DOWN]) < 0 else 0.1)), (True if shift else False))
            _ = player.update_rectangle()

def main():
    global player, map
    #Main game loop
    #Clear the screen, handle the controls (explained above), draw the player (explained above), and update the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Player(int(wWidth/2), int(wHeight/2), pWidth, pHeight)
                    map = Map()
                    main()
        screen.fill(bColor)
        draw_map()
        draw_player()
        handle_controls(pygame.key.get_pressed(), (pygame.key.get_mods() & pygame.KMOD_SHIFT))
        player.x, player.y = map.scroll(player.x, player.y)
        pygame.display.flip()
        clock.tick(tFPS)
#Jump into main loop
main()
