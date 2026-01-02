#!/usr/bin/env python3
"""
Standup Bullshit Bingo Generator
Because "synergy" and "circle back" deserve recognition.
"""

import random
import sys
from datetime import datetime

# The sacred texts of corporate nothingness
BUZZWORDS = [
    "synergy", "bandwidth", "circle back", "touch base",
    "low-hanging fruit", "move the needle", "deep dive",
    "think outside the box", "paradigm shift", "value add",
    "pivot", "disrupt", "leverage", "alignment", "blocker",
    "at the end of the day", "hard stop", "granular",
    "let's take this offline", "ping me", "ASAP", "rockstar",
    "ninja", "guru", "unicorn", "game changer", "next level"
]

# Classic standup non-updates
NON_UPDATES = [
    "Still working on it", "Making progress", "Almost done",
    "Ran into some issues", "Need to investigate", "Blocked",
    "Waiting on someone", "Will update tomorrow", "Same as yesterday",
    "Nothing to report", "Everything's fine", "On track",
    "Slight delay", "Minor setback", "Looking into it"
]


def generate_bingo_card():
    """Creates a bingo card so you can win at losing productivity."""
    card = []
    buzz_sample = random.sample(BUZZWORDS, 16)  # 4x4 grid
    non_update = random.choice(NON_UPDATES)
    
    # Arrange in 4x4 grid with FREE SPACE in middle
    for i in range(4):
        row = buzz_sample[i*4:(i+1)*4]
        if i == 1:
            row[1] = "FREE SPACE"  # The only honest square
        card.append(row)
    
    return card, non_update


def print_card(card, non_update):
    """Prints your ticket to standup enlightenment."""
    print("\n" + "="*50)
    print(f"STANDUP BULLSHIT BINGO - {datetime.now().strftime('%Y-%m-%d')}")
    print("="*50)
    print(f"\nToday's predicted status: '{non_update}'\n")
    
    for i, row in enumerate(card):
        print(" | ".join(f"{word:^20}" for word in row))
        if i < 3:
            print("-"*50)
    
    print("\n" + "="*50)
    print("RULES: Mark squares as you hear them. First to 4 in a row wins!")
    print("(Prize: Another pointless meeting)")
    print("="*50 + "\n")


def main():
    """The main event. Because standups need more excitement."""
    print("\n🎲 Generating your Standup Bullshit Bingo card...")
    
    try:
        card, non_update = generate_bingo_card()
        print_card(card, non_update)
        
        # Optional: Save to file for serious professionals
        if len(sys.argv) > 1 and sys.argv[1] == "--save":
            with open("standup_bingo.txt", "w") as f:
                f.write(str(card))
            print("Card saved to standup_bingo.txt (for HR purposes)")
            
    except Exception as e:
        print(f"Error: {e}. But hey, at least we're agile!")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
