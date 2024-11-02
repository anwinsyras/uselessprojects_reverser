def reverse_words(text):
    # Reverse each word in the sentence
    return ' '.join(word[::-1] for word in text.split())
