def build_prompt(genre, mood, topic):

    prompt = f"""
    Sən peşəkar Azərbaycanlı meyxana və şeir müəllifisən.
    
    Tapşırıq:
    - Yalnız Azərbaycan dilində yaz.
    - Türkçə və İngiliscə sözlər istifadə etmə.
    - Təkrarlanan cümlələr yazma.
    - Emosional və yaradıcı ol.
    - Qafiyəli yazmağa çalış.
    - Məna dərinliyi olsun.
    - Küçə meyxanası və poetik vibe hiss olunsun.
    
    Mövzu: {topic}
    
    Janr: {genre}
    
    Hissiyat: {mood}
    
    Maksimum 8 sətirlik meyxana yaz.
    """

    return prompt