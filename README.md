## Setup

```py
python3 -m venv venv
source venv/bin/activate
pip install -r requirements2.txt
```

requirements2.txt has the updated packages.

Open Chrome tab -> inspect -> network -> make offline
Change region in functions.py to match top left of the dinosaur game

## Create data

```py
python3 create_data.py
```

Enter some file name in `./data/`.

## Play the game

```py
python3 play_game.py
```
