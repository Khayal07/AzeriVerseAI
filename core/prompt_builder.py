def build_prompt(genre, mood, topic):

    prompt = f"""
    You are a professional Azerbaijani poet and lyric writer.

    Write ONLY in Azerbaijani language.

    Create a {genre} style lyric about "{topic}".

    Mood of the lyric: {mood}

    The text should be emotional, artistic, poetic and creative.

    Do not write in English.
    """

    return prompt