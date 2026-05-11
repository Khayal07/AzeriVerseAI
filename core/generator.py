from core.prompt_builder import build_prompt


def generate_lyrics(generator, genre, mood, topic):
    
    prompt = build_prompt(genre, mood, topic)
    
    result = generator(
        prompt,
        max_length = 100,
        num_return_sequences = 1
    )
    
    
    generated_text = result[0]["generated_text"]
    
    return generated_text