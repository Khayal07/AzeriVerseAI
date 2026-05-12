from core.prompt_builder import build_prompt

from utils.text_cleaner import clean_text

from config.settings import (
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_K,
    TOP_P,
    REPETITION_PENALTY
)


def generate_lyrics(generator, genre, mood, topic):
    
    prompt = build_prompt(
        genre,
        mood,
        topic
    )
    
    result = generator(
        
        prompt,
        
        max_new_tokens = MAX_NEW_TOKENS,
        
        do_sample = True,
        
        temperature = TEMPERATURE,
        
        top_k = TOP_K,
        
        top_p = TOP_P,
        
        repetition_penalty = REPETITION_PENALTY,
        
        return_full_text = False
        
    )
    
    generated_text = result[0]["generated_text"]
    
    cleaned_text = clean_text(generated_text)
    
    return cleaned_text