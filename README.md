# CigiYoutube

## Overview

CigiYoutube is a Python application that provides statistics for a specified YouTube channel. It calculates and displays the average views, likes, and comments per video for the channel. The application consists of a Flask backend and a Tkinter GUI for user interaction.

## Features

- Fetches YouTube channel statistics using the YouTube Data API.
- Displays average views, likes, and comments per video.
- Saves the results to a text file.
- Easy-to-use graphical interface built with Tkinter.

## Requirements

- Python 3.6 or higher
- Flask
- Tkinter
- google-api-python-client
- requests

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/youtube-channel-stats.git
cd youtube-channel-stats
```

### Step 2: Create and Configure \`credentials.py\`

Create a file named \`credentials.py\` in the root directory of your project and add your YouTube API key:

```python

# credentials.py

YouTube_Data_API_v3_Key = 'YOUR_YOUTUBE_API_KEY'
```

Replace \`'YOUR_YOUTUBE_API_KEY'\` with your actual YouTube Data API key. This file is included in the \`.gitignore\` to ensure that sensitive information is not tracked by version control.

### Step 3: Install Required Packages

Install the required Python packages using pip:

```bash
pip install Flask google-api-python-client requests
```

### Step 4: Start the Flask Server

Run the Flask server by executing the following command in your terminal:

```bash
python app.py
```

### Step 5: Start the Tkinter GUI

In a new terminal window, run the Tkinter GUI application:

```bash
python gui.py
```

### Step 6: Use the Application

1. **Enter the YouTube Channel ID:**
   In the GUI window, enter the YouTube channel ID for which you want to fetch statistics.

2. **Click "Get Channel Stats":**
   Click the "Get Channel Stats" button. The application will display the average views, likes, and comments per video for the specified channel.

3. **View and Save Results:**
   The results will be displayed in the GUI and also saved to \`channel_stats.txt\` in the root directory of your project.

## Example

- **YouTube Channel ID:** \`XXXXXXXXXXXXXX`
- **Average Views per Video:** 12345.67
- **Average Likes per Video:** 678.90
- **Average Comments per Video:** 12.34

The results will be saved in \`channel_stats.txt\` as:

```
Channel: [Channel Name]
Average Views per Video: 12345.67
Average Likes per Video: 678.90
Average Comments per Video: 12.34

---

```

## File Structure

```
youtube-channel-stats/
│
├── app.py # Flask application
├── gui.py # Tkinter GUI application
├── credentials.py # API key file (excluded from version control)
├── channel_stats.txt # Output file for channel stats (excluded from version control)
├── requirements.txt # Required Python packages
├── .gitignore # Git ignore file
└── README.md # This readme file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Flask](https://flask.palletsprojects.com/)
- [Tkinter](https://wiki.python.org/moin/TkInter)
- [google-api-python-client](https://github.com/googleapis/google-api-python-client)
