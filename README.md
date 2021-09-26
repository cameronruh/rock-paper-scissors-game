# rock-paper-scissors-game

## read me instructions adapted from Prof. Rossetti's example on Github: https://raw.githubusercontent.com/prof-rossetti/my-first-python-app/main/README.md

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this repository: https://github.com/cameronruh/rock-paper-scissors-game under your own control, then download your remote copy onto your local computer and open in VS Code

Then, in the command line, run commands from your local repository's root directory:

```sh
cd rock-paper-scissors-game
```

Use Anaconda to create and activate a new virtual environment, perhaps called "rps-env":

```sh
conda create -n rps-env python=3.8
conda activate rps-env
```

Next, install package dependencies (see the ["requirements.txt"](/requirements.txt) file) through pip install. 

```sh
pip install -r requirements.txt
```

> NOTE: if you see an error such as "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

In the root directory of VS Code, create a new file called ".env", and update the contents of the ".env" file to specify your desired player name (make sure to SAVE the ".env" file):

    PLAYER_NAME="Your Name."

## Usage 

Run the Python Script:

```py
python app/game.py

# alternative module-style invocation (only required if importing from one file to another):
python -m app.game
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.
