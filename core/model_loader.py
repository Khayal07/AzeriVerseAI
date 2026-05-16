import google.generativeai as genai

from config.settings import (
    GEMINI_API_KEY,
    MODEL_NAME
)


def load_generator():

    genai.configure(
        api_key=GEMINI_API_KEY
    )

    model = genai.GenerativeModel(
        MODEL_NAME
    )

    return model