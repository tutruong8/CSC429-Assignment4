from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")

    budget = input("What is your budget? (low/medium/high): ").lower()
    if budget.startswith("l"):
        facts.append("budget_low")
    elif budget.startswith("m"):
        facts.append("budget_medium")
    elif budget.startswith("h"):
        facts.append("budget_high")
    else:
        print("Invalid budget choice. No budget preference will be added.")

    if input("Do you want to play games? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you do creative work (e.g., video editing, graphic design)? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is this laptop for office only? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    
    operating_system = input("What operating system do you prefer? (Windows/macOS/Linux): ").lower()
    if operating_system == "windows" or operating_system.startswith("win"):
        facts.append("os_windows")
    elif operating_system == "macos" or operating_system.startswith("mac"):
        facts.append("os_macos")
    elif operating_system == "linux" or operating_system.startswith("lin"):
        facts.append("os_linux")
    else:
        print("Invalid OS choice. No OS preference will be added.")

    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("ai_accel")
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)
    engine.run()
    conclusions = engine.conclusions()
    print("\nRecommendations:")
    if not conclusions["recommendations"]:
        print("No recommendations could be made based on the provided facts.")  
    else:
        for entry in engine.trace:
            consequent = entry["consequent"]
            if consequent.startswith("recommend:"):
                print(f"Recommendation: {consequent.removeprefix('recommend:')}")
                print(f"Explanation: derived from rule '{entry['rule']}' with antecedents {entry['antecedents']}")
                
    print("\nSpecifications:")
    for spec in conclusions["specs"]:
        print(f"- {spec}")
    print("\nOther Facts:")
    for fact in conclusions["other_facts"]:
        print(f"- {fact}")
    

if __name__ == "__main__":
    main()
