import random

commander = "Commander Flame"

keyword_bank = {
    "primary": ["AI Strategy", "Enterprise Automation", "Ethical AI"],
    "supporting": ["Machine Learning Governance", "LLM Integration", "Risk Mitigation"],
    "long_tail": ["How to deploy AI safely", "AI compliance for small business"]
}

def fire_keyword(mode="primary"):
    selection = keyword_bank.get(mode, ["No intel available"])
    return random.choice(selection)

def confirm_fire():
    confirmation = input(f"{commander}… do I fire? (YES/NO): ").strip().upper()
    if confirmation == "YES":
        return fire_keyword("primary")
    return "Standing by for further orders."

if __name__ == "__main__":
    print(f"🎯 Target Acquired — Pending Flame Authorization")
    response = confirm_fire()
    print(f"🔥 {commander}: {response}")
