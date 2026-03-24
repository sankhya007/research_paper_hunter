def extract_implementation(insights):

    implementations = []

    for s in insights:

        if "model" in s.lower() or "method" in s.lower():
            implementations.append({
                "idea": s,
                "pseudo_code": generate_pseudo_code(s),
                "difficulty": estimate_difficulty(s)
            })

    return implementations


def generate_pseudo_code(text):

    # simple heuristic
    if "panic" in text.lower():
        return "panic += nearby_panic * spread_rate"

    if "speed" in text.lower():
        return "speed *= (1 + panic_factor)"

    return "Implement logic based on description"


def estimate_difficulty(text):

    if "deep learning" in text.lower():
        return "Hard"
    elif "model" in text.lower():
        return "Medium"
    return "Easy"