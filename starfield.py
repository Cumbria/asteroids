import pygame
import random
import math

class StarField:
    def __init__(self, width, height, num_stars=250, layers=3, seed=None):
        if seed is not None:
            random.seed(seed)
        self.width = width
        self.height = height
        self.layers = []
        # each layer contains dicts: pos, size, base brightness, twinkle rate, phase
        for layer_idx in range(layers):
            layer = []
            # more stars in near layers, fewer in far layers
            count = max(8, int(num_stars * (1.0 - layer_idx * 0.25)))
            size = 1 + (layers - layer_idx - 1)  # far layers smaller
            for _ in range(count):
                x = random.uniform(0, width)
                y = random.uniform(0, height)
                base = random.uniform(140, 255) - layer_idx * 30
                rate = random.uniform(0.6, 2.0)
                phase = random.uniform(0, math.pi * 2)
                layer.append({"pos": (x, y), "size": size, "base": base, "rate": rate, "phase": phase})
            self.layers.append(layer)

        # offscreen surface we draw stars onto each frame
        self.surface = pygame.Surface((width, height)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        self.time = 0.0

    def update(self, dt, parallax_dx=0.0, parallax_dy=0.0):
        # dt in seconds; parallax_dx/dy are optional offsets (pixels) to scroll stars for parallax
        self.time += dt
        if parallax_dx or parallax_dy:
            # shift stars by a fraction per layer to create parallax
            for i, layer in enumerate(self.layers):
                mul = (i + 1) / (len(self.layers) + 1)  # nearer layers move more
                for s in layer:
                    x, y = s["pos"]
                    x = (x - parallax_dx * mul) % self.width
                    y = (y - parallax_dy * mul) % self.height
                    s["pos"] = (x, y)


    def draw(self, screen):
        # redraw surface each frame (fill black background so sprites drawn after sit on top)
        self.surface.fill((0, 0, 0))
        t = self.time
        for layer in self.layers:
            for s in layer:
                x, y = int(s["pos"][0]), int(s["pos"][1])
                # twinkle factor between ~0.75 and 1.25
                factor = 0.75 + 0.5 * (0.5 + 0.5 * math.sin(s["phase"] + t * s["rate"]))
                b = int(max(0, min(255, s["base"] * factor)))
                color = (b, b, b, 255)
                pygame.draw.circle(self.surface, color, (x, y), s["size"])
        screen.blit(self.surface, (0, 0))
