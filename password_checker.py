# ============================================================
# PASSWORD STRENGTH CHECKER
# A beginner-friendly Python project using the re (regex) module
# Now with a loop — check as many passwords as you want!
# ============================================================

import re  # Import the 'regex' module for pattern matching


def check_password_strength(password):
    """
    Checks the strength of a given password.
    Returns the strength level and a list of missing conditions.
    """

    # --------------------------------------------------------
    # STEP 1: Define all the conditions a strong password needs
    # re.search() scans the password for each pattern
    # --------------------------------------------------------

    conditions = {
        "At least 8 characters":    len(password) >= 8,
        "Uppercase letter (A-Z)":   bool(re.search(r'[A-Z]', password)),
        "Lowercase letter (a-z)":   bool(re.search(r'[a-z]', password)),
        "Number (0-9)":             bool(re.search(r'[0-9]', password)),
        "Special character (@#$%)": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    # --------------------------------------------------------
    # STEP 2: Separate passed and failed conditions
    # --------------------------------------------------------

    missing = [cond for cond, met in conditions.items() if not met]
    score   = sum(conditions.values())  # Count how many are True

    # --------------------------------------------------------
    # STEP 3: Determine strength based on score
    #   0-2 → Weak | 3-4 → Medium | 5 → Strong
    # --------------------------------------------------------

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, missing


def suggest_improvements(missing):
    """
    Returns a tip for each missing condition.
    """

    tips = {
        "At least 8 characters":    "Make your password longer — use at least 8 characters.",
        "Uppercase letter (A-Z)":   "Add at least one uppercase letter, e.g. A, B, C ...",
        "Lowercase letter (a-z)":   "Add at least one lowercase letter, e.g. a, b, c ...",
        "Number (0-9)":             "Include at least one digit, e.g. 1, 2, 3 ...",
        "Special character (@#$%)": "Add symbols like @ # $ % ^ & * to boost security.",
    }

    return [tips[m] for m in missing if m in tips]


def display_result(password, strength, missing):
    """
    Prints the result clearly in the terminal.
    """

    # Strength label with a visual indicator
    icons = {"Weak": "🔴", "Medium": "🟡", "Strong": "🟢"}
    icon  = icons.get(strength, "")

    print("\n" + "=" * 50)
    print(f"  Password         : {password}")
    print(f"  Password Strength: {icon}  {strength}")
    print("=" * 50)

    # Show missing conditions
    if missing:
        print("\n  Missing Conditions:")
        for item in missing:
            print(f"    ✗  {item}")
    else:
        print("\n  ✓  All conditions met! Great password.")

    # Show improvement tips only if not Strong
    if strength != "Strong":
        suggestions = suggest_improvements(missing)
        if suggestions:
            print("\n  Suggested Improvements:")
            for tip in suggestions:
                print(f"    →  {tip}")

    print("=" * 50)


# ============================================================
# MAIN PROGRAM — Loops until the user chooses to quit
# ============================================================

def main():
    print("\n" + "=" * 50)
    print("       PASSWORD STRENGTH CHECKER")
    print("   Type 'quit' or 'exit' anytime to stop")
    print("=" * 50)

    # --------------------------------------------------------
    # LOOP: Keep asking for passwords until user quits
    # --------------------------------------------------------

    while True:
        # Ask for a password
        password = input("\n  Enter Password (or 'quit' to exit): ").strip()

        # Check if user wants to quit
        if password.lower() in ("quit", "exit", "q"):
            print("\n  👋  Goodbye! Stay secure.\n")
            break

        # Handle empty input
        if not password:
            print("  ⚠   No password entered. Please try again.")
            continue  # Go back to the top of the loop

        # Run the strength check and show result
        strength, missing = check_password_strength(password)
        display_result(password, strength, missing)

        # Ask if they want to check another one
        again = input("\n  Check another password? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  👋  Goodbye! Stay secure.\n")
            break


# ============================================================
# Run main() only when this script is executed directly
# ============================================================

if __name__ == "__main__":
    main()
