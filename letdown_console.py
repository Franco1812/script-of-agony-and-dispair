import time
import os
import sys
from colorama import init, Fore

init(autoreset=True)

chorus_lyrics = [
    "You know, you know where you are with",
    "You know where you are with",
    "Floor collapses, floating",
    "Bouncing back and",
    "One day, I am gonna grow wings",
    "A chemical reaction ",
    "Hysterical and useless ",
    "Hysterical and ",
    "Let down and hanging around",
    "Crushed like a bug in the ground",
    "Let down and hanging around",
]

timings = [
    1.5,  # You know, you know where you are with
    0.9,  # You know where you are with
    0.4,  # Floor collapses, floating
    0.4,  # Bouncing back and
    0.8,  # One day, I am gonna grow wings
    1.0,  # A chemical reaction 
    1.3,  # Hysterical and useless 
    1.3,  # Hysterical and 
    1.3,  # Let down and hanging around
    3.0,  # Crushed like a bug in the ground
    2.0,   # Let down and hanging around
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_cursor(text, delay=0.15):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    """Función principal"""
    try:
        clear_console()
        
        for i, line in enumerate(chorus_lyrics):
            if i < 2:  
                print_with_cursor(line, delay=0.15)
            elif i == 5:  
                print_with_cursor(line, delay=0.13)
            elif i == 6:  
                print_with_cursor(line, delay=0.15)
            else:  
                print_with_cursor(line, delay=0.15)
            
            if i < len(timings):
                time.sleep(timings[i])  
            
    except KeyboardInterrupt:
        print("\n\nReproducción interrumpida")
        sys.exit(0)

if __name__ == "__main__":
    main()