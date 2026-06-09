# QUIZ MASTER – Interactive Quiz Game

An interactive and visually designed Quiz Game built using Python and Kivy/KivyMD.

The game provides a smooth mobile-style experience with multiple screens, level progression, score tracking, leaderboard management, background music, and persistent data storage.

# Project Overview

Quiz Master is a GUI-based quiz application where users answer multiple-choice questions and unlock levels based on performance.
The application is designed with modern UI elements, animated transitions, multimedia integration, and local data persistence.

# Features

## 🏠 Home Screen
- Start Quiz
- View Leaderboard
- Navigation buttons
- Custom game UI

## Quiz System
- Multiple Choice Questions (MCQ)
- Dynamic question loading
- Real-time score updates

## Level Progression
- 50 Level Challenge System
- Unlock next levels
- Progress tracking

## Result System
- Final score display
- Performance feedback

## Leaderboard
- Store player scores
- Rank Users
- Persistent local leaderboard

## Audio Features
- Background music
- Button click sound
- Correct answer sound
- Wrong answer sound

## Data Persistence
- Save progress locally
- Store leaderboard data
- Store unlocked levels


# Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python |
| GUI Framework | Kivy |
| UI Framework | KivyMD |
| Screen Navigation | ScreenManager |
| Data Storage | JSON |
| Dataset Handling | CSV |
| Multimedia | Kivy Audio |
| Event Handling | Event Driven Programming |


# Project Structure

project/

│

├── main.py

├── screens/

│ ├── home.py

│ ├── quiz.py

│ ├── result.py

│ └── leaderboard.py

│

├── assets/

│ ├── images/

│ ├── sounds/

│ └── backgrounds/

│

├── data/

│ ├── questions.csv

│ ├── leaderboard.json

│ └── progress.json

│

└── README.md


# Required Libraries

Install Python packages:

```bash
pip install kivy
pip install kivymd
pip install pandas
```

OR

```bash
pip install kivy kivymd pandas
```


#  System Requirements

- Python 3.10+
- Windows / Linux
- Minimum 4 GB RAM
- Storage: 500 MB+


---

# Game Flow

Home Screen
↓

Start Quiz
↓

Question Screen
↓

Score Calculation
↓

Result Screen
↓

Leaderboard
↓

Next Level

---

# Data Storage

### JSON
Used for:
- Score Storage
- Leaderboard
- Progress Tracking

### CSV
Used for:
- Question Database


# Developer

Developed by:
Vishal Yadav

Project:
QUIZ MASTER