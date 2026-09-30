# SWC2623 Software Development Paradigms
# Coursework 2
# Part C: Multi-Paradigm Programming (Python)
# Integrated Learner Dashboard

import pandas as pd
import subprocess


def run_haskell():
    try:
        result = subprocess.run(
            ["runghc", "test.hs"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except Exception as error:
        return f"Haskell Error: {error}"


print(run_haskell())

def get_haskell_data():
    try:
        result = subprocess.run(
            ["runghc", "test.hs"],
            capture_output=True,
            text=True,
            check=True
        )

        output = result.stdout

        if "PYTHON_DATA" not in output:
            return ""

        return output.split("PYTHON_DATA", 1)[1]

    except Exception as error:
        return f"Haskell Error: {error}"

def parse_haskell_data():
    raw_data = get_haskell_data()
    haskell_data = {}

    for line in raw_data.strip().splitlines():
        parts = line.split("|")

        if len(parts) == 3:
            learner_id = parts[0].strip()
            name = parts[1].strip()

            try:
                average = float(parts[2].strip())
            except ValueError:
                continue

            haskell_data[learner_id] = {
                "name": name,
                "average": average
            }

    return haskell_data


haskell_data = parse_haskell_data()

print("\nHASKELL DATA RECEIVED BY PYTHON")

for learner_id, data in haskell_data.items():
    print(
        learner_id,
        data["name"],
        "| Average:",
        f'{data["average"]:.2f}'
    )

    print()



def run_prolog():
    try:
        goal = (
            "writeln('================================================='),"
            "writeln('PROLOG - MODULE ADVISORY AND CERTIFICATION'),"
            "writeln('================================================='),"
            "nl,"
            
            "writeln('LEARNERS:'),"
            "forall(learner(L,Name),"
            "(write(L),write(' - '),writeln(Name))),"
            "nl,"
            
            "writeln('ELIGIBLE MODULES FOR L001:'),"
            "forall(eligible(l001,Module),writeln(Module)),"
            "nl,"
            
            "writeln('RECOMMENDED MODULES FOR L001:'),"
            "forall(recommend_module(l001,Module),writeln(Module)),"
            "nl,"
            
            "writeln('CERTIFICATION STATUS:'),"
            "forall(learner(L,Name),"
            "(write(L),write(' - '),write(Name),write(' : '),"
            "(eligible_for_certification(L) -> "
            "writeln('Eligible') ; writeln('Not Eligible')))),"
            
            "halt"
        )

        result = subprocess.run(
            [
                "swipl",
                "-q",
                "-s", "test.pl",
                "-g", goal
            ],
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout

    except Exception as error:
        return f"Prolog Error: {error}"
print(run_prolog())

def get_prolog_data():
    try:
        goal = (
            "forall(learner(L,Name),"
            "(findall(M,completed(L,M),Modules),"
            "(eligible_for_certification(L) -> Status='Eligible' ; Status='Not Eligible'),"
            "write(L),write('|'),"
            "write(Name),write('|'),"
            "write(Modules),write('|'),"
            "writeln(Status))),"
            "halt"
        )

        result = subprocess.run(
            [
                "swipl",
                "-q",
                "-s", "test.pl",
                "-g", goal
            ],
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout

    except Exception as error:
        return f"Prolog Error: {error}"

def parse_prolog_data():
    raw_data = get_prolog_data()
    prolog_data = {}

    for line in raw_data.strip().splitlines():
        parts = line.split("|")

        if len(parts) == 4:
            learner_id = parts[0].upper()
            name = parts[1].capitalize()
            modules_text = parts[2].strip("[]")

            if modules_text:
                modules = [
                    module.strip().replace("_", " ").title()
                    for module in modules_text.split(",")
                ]
            else:
                modules = []

            status = parts[3].strip()

            prolog_data[learner_id] = {
                "name": name,
                "completed_modules": modules,
                "certification": status
            }

    return prolog_data


prolog_data = parse_prolog_data()

print("\nPROLOG DATA RECEIVED BY PYTHON")

for learner_id, data in prolog_data.items():
    print(
        learner_id,
        data["name"],
        "| Modules:",
        len(data["completed_modules"]),
        "| Certification:",
        data["certification"]
    )



# ==========================================================
# 1. LEARNER CLASS
# ==========================================================

class Learner:
    def __init__(self, learner_id, name, completed_modules, average):

        if not learner_id or not name:
            raise ValueError("Learner ID and name cannot be empty.")

        if average < 0 or average > 100:
            raise ValueError("Average must be between 0 and 100.")

        self.learner_id = learner_id
        self.name = name
        self.completed_modules = completed_modules
        self.average = average

    def average_score(self):
        return self.average

    def display(self):
        return (
            f"{self.learner_id} - {self.name} | "
            f"Average: {self.average_score():.2f} | "
            f"Performance: {classify_performance(self.average_score())}"
        )


# ==========================================================
# 2. PERFORMANCE CLASSIFICATION
# ==========================================================

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# ==========================================================
# 3. LEARNER DATA
# ==========================================================

learners = [
    Learner(
        "L001",
        haskell_data["L001"]["name"],
        prolog_data["L001"]["completed_modules"],
        haskell_data["L001"]["average"]
    ),

    Learner(
        "L002",
        haskell_data["L002"]["name"],
        prolog_data["L002"]["completed_modules"],
        haskell_data["L002"]["average"]
    ),

    Learner(
        "L003",
        haskell_data["L003"]["name"],
        prolog_data["L003"]["completed_modules"],
        haskell_data["L003"]["average"]
    ),

    Learner(
        "L004",
        haskell_data["L004"]["name"],
        prolog_data["L004"]["completed_modules"],
        haskell_data["L004"]["average"]
    ),

    Learner(
        "L005",
        haskell_data["L005"]["name"],
        prolog_data["L005"]["completed_modules"],
        haskell_data["L005"]["average"]
    )
]


# ==========================================================
# 4. FUNCTIONAL-STYLE OPERATIONS
# ==========================================================

# MAP + LAMBDA
averages = list(
    map(lambda learner: learner.average_score(), learners)
)

# FILTER + LAMBDA
high_achievers = list(
    filter(lambda learner: learner.average_score() >= 80, learners)
)

# LIST COMPREHENSION
learner_names = [
    learner.name for learner in learners
]

# SORTED + LAMBDA
ranked_learners = sorted(
    learners,
    key=lambda learner: learner.average_score(),
    reverse=True
)


# ==========================================================
# 5. INTEGRATED OUTPUT
# ==========================================================

print()
print("=" * 65)
print("INTEGRATED LEARNER DASHBOARD".center(65))
print("=" * 65)

print("\nALL LEARNERS")

for learner in learners:
    print(learner.display())


# ==========================================================
# 6. HIGH ACHIEVERS
# ==========================================================

print("\nHIGH ACHIEVERS (AVERAGE >= 80)")

for learner in high_achievers:
    print(
        f"{learner.learner_id} - "
        f"{learner.name} | "
        f"Average: {learner.average_score():.2f}"
    )


# ==========================================================
# 7. LEARNER RANKING
# ==========================================================

print("\nLEARNER RANKING")

for position, learner in enumerate(ranked_learners, start=1):
    print(
        f"{position}. {learner.name} - "
        f"{learner.average_score():.2f}"
    )


# ==========================================================
# 8. PANDAS SUMMARY TABLE
# ==========================================================

summary_data = [
    {
        "Learner ID": learner.learner_id,
        "Name": learner.name,
        "Completed Modules": len(learner.completed_modules),
        "Average": round(learner.average_score(), 2),
        "Performance": classify_performance(
            learner.average_score()
        ),
        "Certification": prolog_data[
            learner.learner_id
        ]["certification"]
    }
    for learner in learners
]

df = pd.DataFrame(summary_data)

print("\n" + "=" * 75)
print("PANDAS LEARNER SUMMARY".center(75))
print("=" * 75)
print(df.to_string(index=False))


# ==========================================================
# 9. TEST CASES
# ==========================================================

print("\n" + "=" * 65)
print("                       TEST CASES")
print("=" * 65)


# Test 1 - Normal input
print("\nTest 1 - Normal Input")

test1 = Learner(
    "T001",
    "Normal Learner",
    ["Programming Fundamentals"],
    75.0
)

print(test1.display())


# Test 2 - Boundary input
print("\nTest 2 - Boundary Input (Average = 80)")

test2 = Learner(
    "T002",
    "Boundary Learner",
    ["Programming Fundamentals"],
    80.0
)

print(test2.display())


# Test 3 - Low performance
print("\nTest 3 - Low Performance")

test3 = Learner(
    "T003",
    "Low Performance Learner",
    [],
    50.0
)

print(test3.display())


# Test 4 - Invalid input
print("\nTest 4 - Invalid Average")

try:
    test4 = Learner(
        "T004",
        "Invalid Learner",
        [],
        105.0
    )

    print(test4.display())

except ValueError as error:
    print("Input Error:", error)


print("\n" + "=" * 65)
print("                    END OF PROGRAM")
print("=" * 65)