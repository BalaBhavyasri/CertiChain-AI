import re

def clean_ocr_text(text):

    # Remove strange symbols but preserve important ones like + and #
    text = re.sub(r'[^A-Za-z0-9+#:/.,\n -]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Add line breaks after periods
    text = text.replace('. ', '.\n')

    # Remove unnecessary short garbage words (but preserve important short skills)
    words = text.split()

    cleaned_words = []

    for word in words:

        # Keep words > 2 chars OR important technical abbreviations
        if len(word) > 2 or word.lower() in ['c', 'ai', 'ml', 'js', 'db', 'ui', 'ux', 'qa']:
            cleaned_words.append(word)

    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text