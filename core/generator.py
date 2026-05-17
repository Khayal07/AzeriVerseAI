from core.prompt_builder import build_prompt

from utils.text_cleaner import clean_text

from config.settings import MODEL_NAME


def generate_lyrics(generator, genre, mood, topic):

    prompt = build_prompt(
        genre,
        mood,
        topic
    )

    response = generator.models.generate_content(

        model=MODEL_NAME,

        contents=prompt
    )

    generated_text = response.text

    cleaned_text = clean_text(
        generated_text
    )

    return cleaned_text