import sys
import pygame

from settings import Settings
from paddle import Paddle
from paddle_ai import PaddleAI
from ball import Ball
from scoreboard import Scoreboard


class Pong:
    """Overall class managing game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Pong')
        
        self.line_length = self.settings.screen_height // 25
        self.x_middle = self.settings.screen_width // 2
        self.quadrant3 = self.settings.screen_width * 0.75
        self.y_middle = self.settings.screen_height // 2

        self.game_over = False
        self.player_points = 0
        self.ai_points = 0
        
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        # The paddle_ai requires the ball so that it can know its attributes
        self.paddle_ai = PaddleAI(self)
        self.sb = Scoreboard(self)
    
    def run_game(self):
        while not self.game_over:
            self._check_events()
            self.paddle.update()
            self.paddle_ai.update()
            self.ball.update()
            self._check_endgame()
            self._update_screen()

    def _check_endgame(self):
        """Tests if the player or the AI has reached 11 points"""
        if self.player_points >= 11:
            print('Player wins!')
            self.game_over = True
        elif self.ai_points >= 11:
            print('AI wins!')
            self.game_over = True
    
    def _check_events(self):
        """Check for and respond to events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_UP:
            self.paddle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.paddle.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.paddle.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.paddle.moving_down = False

    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        # Redraw the screen at each pass in the loop
        self.screen.fill(self.settings.bg_color)
        self._draw_net()
        self.sb.show_points()
        self.paddle.draw_paddle()
        self.paddle_ai.draw_paddle()
        self.ball.draw_ball()

        # Make the most recently drawn screen visible
        pygame.display.flip()
    
    def _draw_net(self):
        """Draws the dotted net down the center of the screen"""
        # Draw 8 lines
        for i in range(0, 25, 2):
            # Set start and end positions
            y_start_pos = i * self.line_length
            y_end_pos = y_start_pos + self.line_length
            # Draw line
            pygame.draw.line(self.screen, self.settings.paddle_color, (self.x_middle, y_start_pos), (self.x_middle, y_end_pos))


if __name__ == "__main__":
    pong = Pong()
    pong.run_game()