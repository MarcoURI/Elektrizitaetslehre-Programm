# assets
import pygame


# Current code loads images individually
# Suggestion: Create an asset loader class
class AssetLoader:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.images = {}
    
    def load_image(self, name, subfolder=""):
        path = self.base_path / subfolder / f"{name}.png"
        try:
            return pygame.image.load(str(path)).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image {path}: {e}")
            return None