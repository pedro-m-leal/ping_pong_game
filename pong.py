from pygame import *


win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))


class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    # method rawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

ball = GameSprite("add_ball.png", 250, 250, 50, 50, 5) 

run = True
clock = time.Clock()
FPS = 60

while run:
    ball.update()
    ball.reset()
    for e in event.get():  
        if e.type == QUIT:
            run = False
    
    display.update()
    clock.tick(FPS)
