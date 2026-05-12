def build_prompt(genre, mood, topic):

    prompt = f"""
    
    Mövzu: {topic}
    
    Janr: {genre}
    
    Mood: {mood}
    
    Azərbaycan dilində qısa meyxana yaz:
    """

    return prompt