class Settings:
    """A class to store all the settings for Pong"""
    
    def __init__(self):
        """Initialize game's static settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_color = (255, 255, 255)
        self.paddle_width = 10
        self.paddle_height = 75
        self.paddle_speed = 0.25

        # Ball settings
        self.ball_color = (255, 255, 255)
        self.ball_width = 10
        self.ball_height = 10

        self.initial_x_ball_speed = 0.25
        self.initial_y_ball_speed = 0.1
        self.MAX_X_BALL_SPEED = 0.4
        self.MAX_Y_BALL_SPEED = 0.3

        self.x_increment = self.paddle_speed / 4
        self.y_increment = self.paddle_speed / 10