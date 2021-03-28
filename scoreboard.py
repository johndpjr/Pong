import pygame


class Scoreboard:
    """A class to store score information"""

    def __init__(self, pong_game):
        self.pong_game = pong_game
        self.screen = self.pong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.pong_game.settings

        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont('Courier', 28)
        self.prep_points()

    def prep_points(self):
        """Turn the points into a rendered image"""
        # Display player points
        player_points_str = str(self.pong_game.player_points)
        self.player_points_image = self.font.render(player_points_str, True, self.color, self.settings.bg_color)
        self.player_points_rect = self.player_points_image.get_rect()
        self.player_points_rect.left = self.pong_game.x_middle + 30
        self.player_points_rect.top = 20

        # Display AI points
        ai_points_str = str(self.pong_game.ai_points)
        self.ai_points_image = self.font.render(ai_points_str, True, self.color, self.settings.bg_color)
        self.ai_points_rect = self.ai_points_image.get_rect()
        self.ai_points_rect.right = self.pong_game.x_middle - 30
        self.ai_points_rect.top = 20
        
    def show_points(self):
        """Draw both point images to the screen"""
        self.screen.blit(self.player_points_image, self.player_points_rect)
        self.screen.blit(self.ai_points_image, self.ai_points_rect)