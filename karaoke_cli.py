import pygame
import time
import re
from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.panel import Panel

def print_banner():
    banner = """
██    ██  █████  ██████  ██    ██ ████    ██
██    ██ ██   ██ ██   ██ ██    ██ ██ ██   ██
██    ██ ███████ ██████  ██    ██ ██  ██  ██
 ██  ██  ██   ██ ██   ██ ██    ██ ██   ██ ██
  ████   ██   ██ ██   ██  ██████  ██     ███    

                Karaoke Time! 🎤🪩
    """
    console = Console()
    console.print(banner, style="bold green")
    console.print(Panel("Get ready to shine, superstar! ✨", border_style="bold yellow"))

def parse_lrc(filepath):
    lyric_lines = []
    with open(filepath, 'r') as f:
        for line in f:
            matches = re.findall(r'\[(\d+):(\d+\.\d+)\](.+)', line)
            if matches:
                minutes, seconds, lyric = matches[0]
                timestamp = int(minutes) * 60 + float(seconds)
                lyric_lines.append((timestamp, lyric.strip()))
    return lyric_lines

def karaoke(song_path, lrc_path):
    print_banner()
    lyrics = parse_lrc(lrc_path)
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    console = Console()
    console.print("\n[bold yellow]Starting karaoke in 3 seconds. Warm up your vocal cords![/bold yellow] 🎶")
    time.sleep(3)
    pygame.mixer.music.play()
    idx = 0
    start = time.time()
    with Live(auto_refresh=False, console=console) as live:
        while pygame.mixer.music.get_busy():
            now = time.time() - start
            while idx + 1 < len(lyrics) and lyrics[idx + 1][0] <= now:
                idx += 1
            to_display = []
            for i in range(max(0, idx - 1), min(len(lyrics), idx + 2)):
                prefx = "👉 " if i == idx else "   "
                line = lyrics[i][1]
                if i == idx:
                    style = "bold bright_white on magenta"
                    txt = Text(f"{prefx}🎵 {line} 🎵", style=style)
                else:
                    txt = Text(line, style="dim")
                to_display.append(txt)
            live.update(
                Panel(
                    Text("\n".join([str(t) for t in to_display])),
                    title="Sing Along!",
                    border_style="bright_cyan"
                ),
                refresh=True
            )
            time.sleep(0.2)
    console.print("\n[bold magenta]Karaoke finished! Give yourself an ovation![/bold magenta] 👏👏👏")
    console.print(Panel("◉ Thanks for using VARUN KARAOKE! 🎤", border_style="bold red"))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 karaoke_cli.py song.mp3 song.lrc")
    else:
        karaoke(sys.argv[1], sys.argv[2])

