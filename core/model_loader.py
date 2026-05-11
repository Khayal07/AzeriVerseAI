from transformers import pipeline


def load_generator():
    generator = pipeline(
        "text-generation",
        model = "bigscience/bloom-560m"
    )
    
    return generator