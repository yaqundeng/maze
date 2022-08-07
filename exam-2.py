import sys
import pygame

pygame.init()
 
size = width, height = 320, 200
screen = pygame.display.set_mode(size)
window_title = "My game"
pygame.display.set_caption(window_title)

smilie = pygame.image.load("player.png").convert()
##smilie_rect = smilie.get_rect()
##speed = [2, 1]
##black = 0, 0, 0
## 
##smilie = smilie.convert()
##colorkey = smilie.get_at((1,1))
##smilie.set_colorkey(colorkey, pygame.RLEACCEL)
## 
##while True:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            sys.exit()
##            
##    # move object
##    smilie_rect.move_ip(speed)
##    if smilie_rect.left + 10 < 0 or smilie_rect.right - 11 > width:
##        speed[0] = -speed[0]
##    if smilie_rect.top + 10 < 0 or smilie_rect.bottom - 12 > height:
##        speed[1] = -speed[1]
##    pygame.time.delay(10)
##   
##    # update image
##    screen.fill(black)
##    screen.blit(smilie, smilie_rect)
##    pygame.display.flip()

smilie_rect = smilie.get_rect()
print(type(smilie_rect))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# move object
    smilie_rect.move_ip([20, 10])
    pygame.time.delay(100)
# update image
##    screen.blit(smilie, smilie_rect)
##    pygame.display.update()    
##    screen.fill((0, 0, 0))
    screen.blit(smilie, smilie_rect)
    pygame.display.flip()
