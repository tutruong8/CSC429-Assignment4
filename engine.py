from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        if all(antecedent in self.facts for antecedent in rule.antecedents) and rule.consequent not in self.facts:
            return True
        return False

    def run(self) -> None:
        ranked_rules = sorted(self.rules, key=lambda r: (len(r.antecedents), r.priority), reverse=True)
        while True:
            fired = False
            for rule in ranked_rules:
                if self.can_fire(rule):
                    self.facts.add(rule.consequent)
                    self.trace.append({
                        "rule": rule.name,
                        "antecedents": rule.antecedents,
                        "consequent": rule.consequent
                    })
                    fired = True
                    break
            if not fired:
                break

    def conclusions(self) -> Dict[str, List[str]]:
        recommendations = []
        specs = []
        other_facts = []
        for entry in self.trace:
            consequent = entry["consequent"]
            if consequent.startswith("recommend:"):
                recommendations.append(consequent.removeprefix("recommend:"))
            elif consequent.startswith("spec:"):
                specs.append(consequent.removeprefix("spec:"))
            else:
                other_facts.append(consequent)
        
        all_traced_consequents = {entry["consequent"] for entry in self.trace}
        for fact in self.facts:
            if fact not in all_traced_consequents:
                other_facts.append(fact)
        return {
            "recommendations": recommendations,
            "specs": specs,
            "other_facts": sorted(other_facts)
        }