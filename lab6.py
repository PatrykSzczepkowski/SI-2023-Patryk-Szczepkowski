import itertools

def check_consistency(rule, examples):
    consistent_examples = []
    for example in examples:
        if all(example[feature] == value for feature, value in rule):
            consistent_examples.append(example)
    return consistent_examples

def find_rules(examples, max_rule_length):
    num_features = len(examples[0]) - 1
    uncovered_examples = examples.copy()
    rules = []

    for rule_length in range(1, max_rule_length + 1):
        if not uncovered_examples:
            break

        best_rule = None
        best_covered_examples = []

        for rule in itertools.combinations(enumerate(range(num_features)), rule_length):
            covered_examples = check_consistency(rule, uncovered_examples)
            if len(covered_examples) > len(best_covered_examples):
                best_rule = rule
                best_covered_examples = covered_examples

        if best_rule:
            rules.append(best_rule)
            for example in best_covered_examples:
                uncovered_examples.remove(example)

    return rules

decision_system = [
    [1, 1, 1, 1, 3, 1, 1],
    [1, 1, 1, 1, 3, 2, 1],
    [1, 1, 1, 3, 2, 1, 0],
    [1, 1, 1, 3, 3, 2, 1],
    [1, 1, 2, 1, 2, 1, 0],
    [1, 1, 2, 1, 2, 2, 1],
    [1, 1, 2, 2, 3, 1, 0],
    [1, 1, 2, 2, 4, 1, 1]
]

max_rule_length = 2
rules = find_rules(decision_system, max_rule_length)

print("Found rules:")
for rule in rules:
    print(" AND ".join(f"a{feature + 1} = {value}" for feature, value in rule))

def find_rules_without_removing(examples, max_rule_length):
    num_features = len(examples[0]) - 1
    rules = []

    for rule_length in range(1, max_rule_length + 1):
        best_rule = None
        best_covered_examples = []

        for rule in itertools.combinations(enumerate(range(num_features)), rule_length):
            covered_examples = check_consistency(rule, examples)
            if len(covered_examples) > len(best_covered_examples):
                best_rule = rule
                best_covered_examples = covered_examples

        if best_rule:
            rules.append(best_rule)

    return rules

# Use the same decision_system as before
rules_without_removing = find_rules_without_removing(decision_system, max_rule_length)

print("Found rules without removing covered examples:")
for rule in rules_without_removing:
    print(" AND ".join(f"a{feature + 1} = {value}" for feature, value in rule))