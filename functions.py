import random


def reverse_words(text):
    # Reverse each word
    reversed_words = ' '.join(word[::-1] for word in text.split())

    # Randomly change the case of each character
    randomized_case = ''.join(random.choice([char.upper(), char.lower()]) for char in reversed_words)

    # Add a sarcastic comment
    comments = [
        "Well, that was interesting!",
        "Wow, such creativity!",
        "I can’t believe you did that.",
        "You really spent time on this, huh?",
    ]
    sarcastic_comment = random.choice(comments)

    return f"{randomized_case}\n\n{sarcastic_comment}"
