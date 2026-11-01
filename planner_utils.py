
def calculate_budget(budget):
    """Calculate estimated event budget allocations."""
    if not isinstance(budget, (int, float)):
        raise TypeError("Budget must be a number.")

    if budget < 500:
        raise ValueError("Budget must be at least ₹500.")

    return {
        "Venue": budget * 0.30,
        "Food & Drinks": budget * 0.35,
        "Decorations": budget * 0.20,
        "Other": budget * 0.15
    }


def get_demo_ideas(kind, chosen_theme, guests, special):
    """Generate built-in event suggestions."""

    ideas = {
        "Birthday Party": [
            "Create a photo backdrop and cake table.",
            "Plan music, party games and group photos.",
            "Send invitations and confirm the guest list."
        ],
        "College Fest": [
            "Prepare a stage schedule and assign volunteers.",
            "Plan student activities and registration.",
            "Confirm sound, seating and venue arrangements."
        ],
        "Farewell Party": [
            "Create a memory wall with photos.",
            "Plan speeches, music and a slideshow.",
            "Arrange refreshments and group photographs."
        ],
        "Anniversary": [
            "Create a photo timeline of memories.",
            "Plan a themed meal and decorations.",
            "Prepare a memory-sharing activity."
        ],
        "Wedding": [
            "Prepare a venue and guest checklist.",
            "Coordinate food and decorations.",
            "Assign event-day responsibilities."
        ],
        "Graduation Party": [
            "Create a graduation photo corner.",
            "Plan speeches and a celebration playlist.",
            "Arrange snacks and group photos."
        ],
        "Festival Celebration": [
            "Choose suitable festival decorations.",
            "Plan food, music and group activities.",
            "Prepare setup and cleanup checklists."
        ],
        "Other Celebration": [
            "Choose a suitable venue and theme.",
            "Plan food, decorations and activities.",
            "Prepare invitations and a schedule."
        ]
    }

    result = ideas.get(kind, ideas["Other Celebration"])

    result = result + [
        f"Plan for approximately {guests} guests and stay within budget."
    ]

    if special and special.strip():
        result.append(f"Special request: {special.strip()}.")

    return result
