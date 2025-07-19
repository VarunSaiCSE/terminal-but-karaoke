# Terminal but Karaoke 🎤

A fun, hackable terminal karaoke machine that syncs lyrics with your music and adds ASCII art and color to your shell!

## 📦 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup \& Installation](#setup--installation)
5. [Usage Instructions](#usage-instructions)
6. [Adding Your Own Songs](#adding-your-own-songs)
7. [Troubleshooting](#troubleshooting)
8. [Project Structure](#project-structure)
9. [Credits](#credits)

## 🧑‍💻 Overview

This project transforms your terminal into a karaoke machine powered by Python. It plays your chosen song, shows a vibrant ASCII banner, and synchronizes lyrics in real-time—all in the command line. Great for hackathons, demos, or just singing for fun!

## ✨ Features

- Plays mp3 (or wav) audio in the terminal
- Displays lyrics in sync using `.lrc` lyric files
- Fun and customizable ASCII art banners
- Colorful and animated terminal experience
- Easy setup and portable code


## 🛠 Requirements

- **Python 3.x** (most macOS/Linux systems have this pre-installed)
- Python packages: `pygame`, `rich`


## 🚀 Setup \& Installation

Clone this repository or download the project files, then open your terminal and follow these steps:

### 1. Go to the Project Directory

Move into the folder where this README and the code/script live:

```sh
cd /path/to/karaoke-cli
```

*(You can also type `cd `, then drag and drop the folder onto your terminal window.)*

### 2. Install Dependencies

If you see a `requirements.txt` file, run:

```sh
pip3 install -r requirements.txt
```

Or install packages individually:

```sh
pip3 install pygame rich
```


## 🎵 Usage Instructions

### 1. Make Sure You Have:

- The main script: `karaoke_cli.py`
- At least one `.mp3` music file (e.g., `song.mp3`)
- A matching `.lrc` lyric file (e.g., `song.lrc`)

All files should be in the **same folder**.

### 2. Run the Karaoke Script

Replace `song.mp3` and `song.lrc` with your file names as needed:

```sh
python3 karaoke_cli.py song.mp3 song.lrc
```

- The banner will appear
- After a short countdown, your song will play and lyrics will start scrolling
- **Press `Ctrl + C` at any time to stop**


## 🎶 Adding Your Own Songs

1. **Get an audio file:**
Use any `.mp3` or `.wav` file you own or have rights to.
2. **Find or create a matching `.lrc` file:**
`.lrc` files have time-stamped lyrics lines. Example:

```
[00:05.00]Twinkle, twinkle, little star
[00:10.00]How I wonder what you are
```

3. **Place both your audio file and its `.lrc` in the project folder.**
4. **Run:**

```sh
python3 karaoke_cli.py your_song.mp3 your_song.lrc
```


## 🧩 Troubleshooting

- **No output?**
    - Make sure you are calling the script with both the audio and lyrics filenames as arguments.
- **File not found?**
    - Double-check spelling and file extensions.
    - Files must be in the current directory.
- **Dependencies missing?**
    - Rerun: `pip3 install pygame rich`
- **Lyrics out of sync?**
    - Verify your `.lrc` timestamps match the actual song.


## 📂 Project Structure

```
karaoke-cli/
├── karaoke_cli.py         # Main karaoke script
├── song.mp3               # Sample audio (replace with your own)
├── song.lrc               # Sample lyrics file (replace with your own)
├── requirements.txt       # Python dependencies
├── README.md              # This documentation
└── .gitignore             # Standard git ignore file
```


## 👥 Credits

Written by Varun Sai Andra, For the Love of Code, 19 July 2025.

> Enjoy your terminal karaoke session! PRs and forks welcome.
> For questions, raise an issue or reach out!
> andra.varunsai@gmail.com
