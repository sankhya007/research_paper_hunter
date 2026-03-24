def extract_insights(text):

    sentences = text.split("\n")

    important = []

    for s in sentences:

        s_low = s.lower()

        if any(k in s_low for k in [
            "equation", "formula", "=",  # formulas
            "we propose", "we introduce", "model", "method",
            "algorithm", "approach",
            "implementation", "we implement",
            "results show", "experiment"
        ]):
            important.append(s.strip())

    return important[:20]


def detect_uniqueness(insights):
    for s in insights:
        if "novel" in s.lower() or "first" in s.lower():
            return s
    return insights[0] if insights else ""