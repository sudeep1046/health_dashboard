def get_recommendations(heart_rate, steps, sleep_hours):
    recs = []

    # Heart rate checks
    if heart_rate < 60:
        recs.append("Your heart rate is low. Consider light activity like walking.")
    elif heart_rate > 100:
        recs.append("High heart rate detected. Take rest and stay hydrated.")
    else:
        recs.append("Your heart rate is normal. Keep it up!")

    # Steps checks
    if steps < 5000:
        recs.append("Try to walk at least 7,000–10,000 steps a day.")
    else:
        recs.append("Great! You're staying active.")

    # Sleep checks
    if sleep_hours < 6:
        recs.append("You should aim for 7–9 hours of sleep.")
    else:
        recs.append("Good job! You're getting enough sleep.")

    return recs
