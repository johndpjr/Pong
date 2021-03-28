import pygame


class Paddle:
    """Models the player-controlled paddle"""

    def __init__(self, pong_game):
        """Initialize the paddle at its starting position"""
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.color = self.settings.paddle_color
        self.screen_rect = pong_game.screen.get_rect()

        # Movement flag
        self.moving_up = False
        self.moving_down = False

        # Draw the paddle rectangle and set its starting position to the middle
        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.rect.midright = self.screen_rect.midright

        # Paddle y position
        self.y = float(self.rect.y)
    
    def update(self):
        """Update the paddle's position based on the movement flag"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.paddle_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed
        
        # Update rect object to y position
        self.rect.y = self.y
    
    def draw_paddle(self):
        """Draw the paddle to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)