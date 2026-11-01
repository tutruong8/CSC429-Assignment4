from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    if input("Do you want to play games? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you do creative work (e.g., video editing, graphic design)? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is this laptop for office only? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    if input("What is your preferred operating system? (Windows/macOS/Linux): ").lower() == "windows":
        facts.append("os_windows")
    elif input("What is your preferred operating system? (Windows/macOS/Linux): ").lower() == "macos":
        facts.append("os_macos")
    else:
        facts.append("os_linux")
    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("ai_accel")
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    pass

if __name__ == "__main__":
    main()
