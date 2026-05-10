from transformers import pipeline


def load_generator():
    generator = pipeline(
        "text-generation",
        model = "gpt2"
    )
    
    return generator