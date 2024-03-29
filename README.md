# JARVIS (Just a Rather Very Intelligent System)

It can do a lot of cool things, some of them being:

- Greet user
- Tell current time and date
- Launch applications/softwares
- Open any website
- Tells about weather of any city
- Open location of any place plus tells the distance between your place and queried place
- Tells your current system status (RAM Usage, battery health, CPU usage)
- Tells about your upcoming events (Google Calendar)
- Tells about any person (via Wikipedia)
- Can search anything on Google
- Can play any song on YouTube
- Tells top headlines (via Times of India)
- Plays music
- Send email (with subject and content)
- Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)
- Answer any generic question (via Wolframalpha)
- Take important note in notepad
- Tells a random joke
- Tells your IP address
- Can switch the window
- Can take screenshot and save it with custom filename
- Can hide all files in a folder and also make them visible again
- Has a cool Graphical User Interface

## API Keys

To run this program you will require a bunch of API keys. Register your API key by clicking the following links

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Wolframalpha](https://www.wolframalpha.com/)
- [Google Calendar API](https://developers.google.com/calendar/auth)

## Installation

- First clone the repo
- Make a config.py file and include the following in it:
  ```weather_api_key = "<your_api_key>"
  email = "<your_email>"
  email_password = "<your_email_password>"
  wolframalpha_id = "<your_wolframalpha_id>"
  ```
- Copy the config.py file in Jarvis>config folder
- Make a new python environment
  If you are using anaconda just type `conda create -n jarvis python==3.8.5 ` in anaconda prompt
- To activate the environment `conda activate jarvis`
- Navigate to the directory of your project
- Install all the requirements by just hitting `pip install -r requirements.txt`
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by `python main.py`
- Enjoy !!!!

## Code Structure

    ├── driver
    ├── Jarvis              # Main folder for features
    │   ├── config          # Contains all secret API Keys
    │   ├── features        # All functionalities of JARVIS
    │   └── utils           # GUI images
    ├── __init__.py         # Definition of feature's functions
    ├── gui.ui              # GUI file (in .ui format)
    ├── main.py             # main driver program of Jarvis
    ├── requirements.txt    # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable
- To add a new feature:
  - Make a new file in features folder, write the feature's function you want to include
  - Add the function's definition to **init**.py
  - Add the voice commands through which you want to invoke the function

It was in my Mini Project - II(Semester-5)

- Project Synopsis - https://drive.google.com/file/d/1P85K2g96QAKk-4wKkhlWhwc_HhlnNe90/view?usp=drive_link
- Project Report - https://drive.google.com/file/d/1_AFPg2wBzxGqvZ2dalO8to20asuNPYut/view?usp=drive_link
- Project PPT - https://docs.google.com/presentation/d/1TQComlY8cToiARaw5kKocZVcn6FtAZHJ/edit?usp=sharing&ouid=109226689315072486930&rtpof=true&sd=true

# Project Recognition 🏆

JARVIS was developed as part of the Mini Project II for Semester 5 and was recognized as a runner-up project in the CVMU Hackathon. The project's synopsis, report, and presentation slides are available for further reference.

## Additional Features:

- **Gaming Modules**: Includes popular games like Temple Run and Subway Surfers integrated with body movement controls for an immersive experience.

- **Interactive Games**: Offers narrative-based games such as number guessing and rock-paper-scissors for interactive entertainment.

- **Real-Time Translator**: Facilitates communication by providing real-time translation capabilities.

JARVIS aims to provide users with a comprehensive and intuitive interface for performing various tasks efficiently and enjoying entertainment options seamlessly.

![alt text](image.png)
