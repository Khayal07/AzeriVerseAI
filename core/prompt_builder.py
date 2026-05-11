def build_prompt(genre, mood, topic):

    prompt = f"""
    Azərbaycan dilində yaz.
    
    Mövzu: {topic}
    
    Janr: {genre}
    
    Mood: {mood}
    
    Qısa və yaradıcı sözlər yaz:
    """

    return prompt