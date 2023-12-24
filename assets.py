import os
import pygame
sprites = {}


def load_sprites():
    path = os.path.join('assets', 'sprites')
    for filename in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(
            os.path.join(path, filename))
