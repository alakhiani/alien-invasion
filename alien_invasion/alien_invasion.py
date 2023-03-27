import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage the game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()

        # Clock used to control the frame rate and ensure the game is running smoothly
        self.clock = pygame.time.Clock()

        # Initialize the game settings
        self.settings = Settings()

        # Create the game's main surface and set a caption
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # (self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height        
        pygame.display.set_caption("Alien Invasion")

        # Initialize the ship object
        self.ship = Ship(self)
        
        # Initialize a group for the bullets
        self.bullets = pygame.sprite.Group()
        

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self) -> None:
        """ Respond to keypress and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False        
                    
    def _update_screen(self) -> None:
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
