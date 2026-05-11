from core.prompt_builder import build_prompt
from utils.text_cleaner import clean_text


def generate_lyrics(generator, genre, mood, topic):
    
    prompt = build_prompt(genre, mood, topic)
    
    result = generator(
        prompt,
        max_new_tokens = 120,
        do_sample = True,
        temperature = 0.9,
        top_k = 50,
        top_p = 0.95,
        repetition_penalty = 1.2,
    )
    
    
    generated_text = result[0]["generated_text"]
    
    cleaned_text = clean_text(generated_text)
    
    return cleaned_text