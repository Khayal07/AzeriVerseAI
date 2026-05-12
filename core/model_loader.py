from transformers import pipeline

from config.settings import MODEL_NAME


def load_generator():
    
    generator = pipeline(
        "text-generation",
        model = MODEL_NAME
    )
    
    return generator