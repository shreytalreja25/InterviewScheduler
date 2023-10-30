import time
from art import *
from halo import Halo

def hack_user_calendar():
    # Simulating access to the user's calendar
    spinner = Halo(text='Accessing user\'s calendar', spinner='dots')
    spinner.start()
    time.sleep(2)
    spinner.succeed()

    # Simulating setting up the interview event
    spinner = Halo(text='Setting up the interview event', spinner='dots')
    spinner.start()
    time.sleep(2)
    spinner.succeed()

    # Simulating ensuring automatic participation
    spinner = Halo(text='Ensuring automatic participation', spinner='dots')
    spinner.start()
    time.sleep(2)
    spinner.succeed()

    print("Interview scheduled successfully!")

# Schedule the interview for Saturday, 4th September, 4:00 PM.
interview_date = "4th September 2023, 4:00 PM"

# Natwest Bank Logo in ASCII art
natwest_logo = r"""
   _____ _          _ _       _     _           
  / ____| |        | | |     | |   | |          
 | (___ | |__   ___| | | __ _| |__ | | ___  ___ 
  \___ \| '_ \ / _ \ | |/ _` | '_ \| |/ _ \/ __|
  ____) | | | |  __/ | | (_| | | | | |  __/\__ \
 |_____/|_| |_|\___|_|_|\__,_|_| |_|_|\___||___/
"""

# Print the Natwest Bank Logo and Name
print(natwest_logo)
print("Natwest Bank")
result = text2art("Interview Scheduler", font='block')
print(result)
print(f"Scheduling the interview for {interview_date}...")

# Simulating the countdown
spinner = Halo(text='Simulating the countdown', spinner='dots')
spinner.start()
time.sleep(2)
spinner.succeed()

# Run the simulated hacking script
hack_user_calendar()
