from openai import OpenAI

from config.settings import (
    OPENROUTER_API_KEY
)


def load_generator():

    client = OpenAI(

        api_key=OPENROUTER_API_KEY,

        base_url="https://openrouter.ai/api/v1"
    )

    return client