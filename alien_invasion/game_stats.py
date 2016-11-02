class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """initialise statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start in an inactive state
        self.game_active = False
        #high score shouldn't get reset
        self.high_score = 0

    def reset_stats(self):
        """initialise stats that can change through the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
