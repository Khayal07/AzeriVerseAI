from core.model_loader import load_generator

from core.generator import generate_lyrics

from utils.dataset_loader import load_dataset

from config.settings import (
    APP_NAME,
    APP_VERSION
)


print(f"{APP_NAME} v{APP_VERSION}")

print("\nLoading dataset...")

dataset = load_dataset("data/raw/meyxana.txt")

print("Dataset loaded successfully!")

print("\nDataset Preview:\n")

print(dataset[:200])

print("\n----------------------\n")

print("Connecting to AI API...")

generator = load_generator()

print("AI API connected successfully!")

genre = "meyxana"

mood = "dark"

topic = "sevgi"

print("\nGenerating lyrics...\n")

try:

    lyrics = generate_lyrics(
        generator,
        genre,
        mood,
        topic
    )

    print("Generated Meyxana:\n")

    print(lyrics)

except Exception as error:

    print("Generation Error:")

    print(error)