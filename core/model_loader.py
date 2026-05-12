from openai import OpenAI

from config.settings import (
    TOGETHER_API_KEY
)


def load_generator():
    
    client = OpenAI(
        
        api_key = TOGETHER_API_KEY,
        
        base_url = "https://api.together.xyz/v1"
        
    )
    
    return client