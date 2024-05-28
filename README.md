# Telegram bot for workouts

This bot is designed to keep track of user's workouts. It allows you to keep statistics on different exercises (abs, bars, push-ups, pull-ups) and get total statistics for the whole time, as well as detailed statistics on each exercise for different days.

## Installation

1. `git clone https://github.com/zachey01/WorkoutBot.git`
2. Rename `config.py.example` to `config.py` and paste Telegram token
3. `pip install -r requirements.txt`
4. `py main.py`
5. Enjoy ^^

## Main Functions

### Adding data

1. Click on one of the four buttons: abs, bars, push-ups, pull-ups.
2. Select the number of reps for this exercise by selecting one of the options from the menu.
3. The data will be automatically saved and added to your statistics for the current day.

### Retrieving Statistics

- Click the “Statistics” button to get your total statistics for the entire workout.
- Click the “Detailed Statistics” button to get statistics for each exercise for different days.

### Cancel operation

- You can press the “Cancel” button at any time to return to the main menu.

### Example of use

1. User starts a chat with the bot.
2. The user selects the “Press” exercise and enters the number of reps, e.g. 15.
3. The bot saves the workout data.
4. The user can request their stats, such as the total number of presses for the entire time.

## Note

- The bot automatically creates a new record for each workout day.
- For each exercise, an array is stored with the number of repetitions for each workout.
