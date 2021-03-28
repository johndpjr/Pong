import pygame

from paddle import Paddle


class PaddleAI(Paddle):
    """Controls the AI that responds to ball movement"""

    def __init__(self, pong_game):
        super().__init__(pong_game)
        self.rect.midleft = self.screen_rect.midleft
        self.pong_game = pong_game
        self.ball = self.pong_game.ball
    
    def update(self):
        """If the ball at or past quadrant3, move the paddle to intercept it"""
        if self.ball.x <= self.pong_game.quadrant3 and self.ball.x_direction == -1:
            if self.ball.y < self.y or self.rect.top < self.screen_rect.top:
                self.y -= self.pong_game.settings.paddle_speed
            elif self.ball.y > self.y or self.rect.bottom < self.screen_rect.bottom:
                self.y += self.pong_game.settings.paddle_speed
        
        # Update rect object to y position
        self.rect.y = self.y