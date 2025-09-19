
# Space Enforcers

## Game Description

Space Enforcers is a fast-paced, single-player spaceship battle game. You control a spaceship and compete to score hits on your opponent. The game features vibrant graphics and sound effects for an engaging experience. Power-ups and multiplayer modes are not available at this time.

## How to Play

1. **Objective:**
   - Defeat your opponent by scoring more hits and reducing their health to zero.

2. **Controls:**
   - Use the keyboard to move your spaceship and fire weapons.
   -Arrow keys to move and space bar to fire.

3. **Game Modes:**
   - Single-player mode only availble at this time.
   - Select your preferred mode from the main menu.

4. **Weapons:**
   - Use your weapons strategically to outmaneuver and defeat your opponent.

5. **Winning:**
   - The player with the highest score or last spaceship standing wins the round best of 3.

## Setup

1. **Activate the virtual environment:**
   ```sh
   source bin/activate
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Game

1. Make sure the virtual environment is activated.
2. Run the main script:
   ```sh
   python init.py
   ```

## Troubleshooting

- If you see `ModuleNotFoundError: No module named 'pygame'`, make sure you have activated the virtual environment and installed dependencies.
- If you encounter other errors, check that all assets are present in the `Asset_Project_1` folder.

## Project Structure

- `init.py` - Main entry point
- `Settings.py` - Game settings and initialization
- `Game_mode.py` - Game mode logic
- `Asset_Project_1/` - Images, sounds, and other assets
- `requirements.txt` - Python dependencies

## Requirements

See `requirements.txt` for all required Python packages.

---

Enjoy playing Space Enforcers!
