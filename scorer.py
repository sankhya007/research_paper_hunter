def score_paper(paper, insights):
    
    relevance = len(paper["abstract"] or "")
    novelty = sum(1 for i in insights if "novel" in i.lower())
    implementation = len(insights)

    score = (
        0.4 * relevance +
        2.0 * novelty +
        1.5 * implementation
    )

    return round(score, 2)