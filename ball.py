import pygame
import time


class Ball:
    """Models the ball that moves from left to right"""

    def __init__(self, pong_game):
        """Initialize the ball at its starting position (center)"""
        self.pong_game = pong_game
        self.screen = self.pong_game.screen
        self.settings = self.pong_game.settings
        self.color = self.settings.ball_color
        self.screen_rect = self.pong_game.screen.get_rect()

        # Draw the paddle rectangle and set its starting position to the middle
        self.rect = pygame.Rect(0, 0, self.settings.ball_width, self.settings.ball_height)
        self.rect.center = self.screen_rect.center
        
        self.reset_ball()

    def reset_ball(self):
        """Reset ball speed and position"""

        # Paddle x and y positions
        self.x = float(self.screen_rect.center[0])
        self.y = float(self.screen_rect.center[1])

        # x_direction of 1 means right; -1 means left
        self.x_direction = 1
        # y_direction of 1 means down; -1 means up
        self.y_direction = 1

        # Set inital x and y speeds of the ball to setting defaults
        self.x_speed = self.settings.initial_x_ball_speed
        self.y_speed = self.settings.initial_y_ball_speed

        self.ball_out = False

    def _prep_ball(self):
        """Preps a ball for resetting after a point has been scored"""
        self.ball_out = True
        self.pong_game.sb.prep_points()
        time.sleep(1)
        self.reset_ball()
    
    def update(self):
        """Update the ball's position based on the movement flag"""
        self._check_all_collisions()
        # Check if the direction is right (positive), else move left
        if self.x_direction == 1:
            self.x += self.x_speed
        else:
            self.x -= self.x_speed
        
        # Check if the direction is down (positive), else move up
        if self.y_direction == 1:
            self.y += self.y_speed
        else:
            self.y -= self.y_speed
        
        # Update rect object to x and y position
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw_ball(self):
        """Draw the paddle to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def _check_all_collisions(self):
        self._check_edge_collision()
        self._check_paddle_collision()
        self._check_wall_collision()
    
    def _check_edge_collision(self):
        """Adds point and resets ball if there is a collision with the edge"""
        if not self.ball_out:
            # Ball goes out on the right side: AI gains a point
            if self.rect.left >= self.screen_rect.right:
                self.pong_game.ai_points += 1
                self._prep_ball()
            # Ball goes out on the left side: player gains a point
            if self.rect.right <= 0:
                self.pong_game.player_points += 1
                self._prep_ball()
    
    def _check_paddle_collision(self):
        """Negates x_direction if there is a collision with the paddle"""
        if self.rect.colliderect(self.pong_game.paddle.rect) or self.rect.colliderect(self.pong_game.paddle_ai.rect):
            # If the paddle is moving, add speed to the y direction
            if self.pong_game.paddle.moving_up or self.pong_game.paddle.moving_down:
                if self.x_speed < self.settings.MAX_X_BALL_SPEED:
                    self.x_speed += self.settings.x_increment
                if self.y_speed < self.settings.MAX_Y_BALL_SPEED:
                    self.y_speed += self.settings.y_increment
            self.x_direction *= -1

    def _check_wall_collision(self):
        """Negates y_direction if there is a collision with the wall (top or bottom screen)"""
        if self.rect.top <= self.screen_rect.top or self.rect.bottom >= self.screen_rect.bottom:
            self.y_direction *= -1