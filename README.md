# Asteroids (StressFree Gaming)

Classic Asteroids-style arcade game implemented in Python using Pygame.

## Motivation

Teach myself Python after not using it since College. The language itself is very straightforward. 
It didn't take me long to adapt from JS and C# back to Python. I enjoyed getting to grips with this "old friend."

## Quick start

Requirements
- Python >= 3.12 (see [.python-version](.python-version))
- Pygame 2.6.1 (see [pyproject.toml](pyproject.toml))

Run the game:
```sh
python main.py
```

The game entrypoint is [`main.main`](main.py).

## Usage / Controls

- W / S — thrust forward / reverse
- A / D — rotate left / right
- Space — fire

## Features

- Simple physics-based movement and rotation
- Multiple asteroid sizes and splitting behaviour
- Shots with rainbow colours
- Starfield background with parallax + twinkle
- Score tracking and high score persistence
- Lightweight event/state logging for debugging

Key behaviors are implemented in:
- Player: [`player.Player`](player.py)  
- Asteroid: [`asteroid.Asteroid`](asteroid.py)  
- Asteroid spawn manager: [`asteroidfield.AsteroidField`](asteroidfield.py)  
- Generic circle sprite base: [`circleshape.CircleShape`](circleshape.py)  
- Shots: [`shots.Shots`](shots.py)  
- Score persistence/UI: [`score.Score`](score.py)  
- Background: [`starfield.StarField`](starfield.py)  
- Logging helpers: [`logger.log_state`](logger.py), [`logger.log_event`](logger.py)  
- Constants: [`constants`](constants.py)

## Files in this repository

- [.gitignore](.gitignore)  
- [.python-version](.python-version)  
- [asteroid.py](asteroid.py)  
- [asteroidfield.py](asteroidfield.py)  
- [circleshape.py](circleshape.py)  
- [constants.py](constants.py)  
- [highscore.txt](highscore.txt)  
- [logger.py](logger.py)  
- [main.py](main.py)  
- [player.py](player.py)  
- [pyproject.toml](pyproject.toml)  
- [README.md](README.md)  
- [score.py](score.py)  
- [shots.py](shots.py)  
- [starfield.py](starfield.py)  

## Development notes

- Sprite classes subclass [`circleshape.CircleShape`](circleshape.py) and register themselves with pygame groups in `main.py`.
- Logging writes compact JSONL snapshots to [game_state.jsonl](game_state.jsonl) and events to [game_events.jsonl](game_events.jsonl).
- High score is stored in [highscore.txt](highscore.txt) (loaded/written by [`score.Score`](score.py)).

## Tuning

Common constants are in [`constants.py`](constants.py) (player speed, turn speed, spawn rate, radii).

## Contributing

- Fixes, improvements and bug reports via issues and pull requests.
- No other contributors.

## License

There is no license for this repo. Feel free to play around.
