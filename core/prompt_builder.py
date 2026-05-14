def build_prompt(genre, mood, topic):

    prompt = f"""
    Mövzu: {topic}

    Janr: {genre}

    Hiss: {mood}

    Azərbaycan dilində yaradıcı və emosional meyxana yaz.

    Qafiyəli və mənalı olsun.
    """

    return prompt