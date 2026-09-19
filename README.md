# Rave's Python Pig Game

A command-line implementation of the classic **Pig** dice game for 2 or more players. Players roll a six-sided die to build points during a turn, then choose whether to hold their points or risk another roll. And the first player to reach the selected score wins.

## Configuration

The game has some set of configurations stored in the `CONFIG` dictionary near the top of `pig.py` code that configures and changes how the game runs:

| Setting | Default | Description |
| --- | ---: | --- |
| `default_goal` | `100` | Score required to win when the default goal is selected. |
| `max_players` | `5` | Highest player count allowed by the code. |
| `roll_limit` | `4` | Maximum number of turn-loop iterations before points are returned automatically. |
| `withdrawal-point` | `5` | Points deducted from a player's total after rolling a `1`. |
| `1-point-word` | `unlocky` | Message displayed when a player rolls a `1`. |

## Gameplay

1. Type your target score or `d` for default score (the default is `100`).
2. Input the number of players.
3. On each turn, choose:
   - `r` or `roll` to roll the die.
   - `h` or `hold` to bank the points earned during that turn.
4. Rolling a `1` ends the turn, discards that turn's unbanked points, and deducts 5 points from the player's total score.
5. The first player whose total score reaches the target score wins.

The game also caps a turn at four roll/hold prompts, as configured by `roll_limit`.

## Requirements

- Python 3.10 or later.
- [`pyfiglet`](https://pypi.org/project/pyfiglet/) for the start-up banner.

## Installation

> Clone the Repository.
```bash
git clone https://github.com/Rave-codes-67/python-pig-game
```

> Change directory to the cloned local repository
```bash
cd "Pig Game"
```

> Create a Virtual Environment
```bash
python -m venv .venv
```

> Activate the virtual environment:
```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\Activate.bat

# macOS / Linux
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install pyfiglet
```

## Run

Start the game with:

```bash
python3 pig.py
```


## License

This project is licensed under the [MIT License](LICENSE).