from core.prompt_builder import build_prompt

from utils.text_cleaner import clean_text

from config.settings import MODEL_NAME


def generate_lyrics(generator, genre, mood, topic):

    prompt = build_prompt(
        genre,
        mood,
        topic
    )

    response = generator.chat.completions.create(

    model=MODEL_NAME,

    messages=[

        {
            "role": "user",
            "content": prompt
        }
    ],

    temperature=1,

    max_tokens=120
)

    generated_text = response.choices[0].message.content

    cleaned_text = clean_text(generated_text)

    return cleaned_text