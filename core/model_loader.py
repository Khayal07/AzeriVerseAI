from google import genai

from config.settings import GEMINI_API_KEY


def load_generator():

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    return client