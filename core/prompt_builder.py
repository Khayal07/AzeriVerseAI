def build_prompt(genre, mood, topic):

    prompt = f"""
    Sən peşəkar Azərbaycanlı meyxana və şeir müəllifisən.

    Qaydalar:
    - Yalnız Azərbaycan dilində yaz.
    - Türkçə istifadə etmə.
    - İngiliscə istifadə etmə.
    - Təkrarlanan cümlələr yazma.
    - Qafiyəli və emosional yaz.
    - Küçə meyxanası atmosferi hiss olunsun.

    Mövzu: {topic}

    Janr: {genre}

    Hissiyat: {mood}

    Maksimum 8 sətirlik meyxana yaz.
    """

    return prompt