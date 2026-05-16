from utils.logger import logger

from core.model_loader import load_generator

from core.generator import generate_lyrics

from utils.dataset_loader import load_dataset

from config.settings import (
    APP_NAME,
    APP_VERSION
)


print(f"{APP_NAME} v{APP_VERSION}")

logger.info("Loading dataset...")

dataset = load_dataset("data/raw/meyxana.txt")

print("Dataset loaded successfully!")

print("\nDataset Preview:\n")

print(dataset[:200])

print("\n----------------------\n")

logger.info("Connecting to AI API...")

generator = load_generator()

print("AI API connected successfully!")

genre = "meyxana"

mood = "aggressive"

topic = "küçə həyatı"

logger.info("Generating lyrics...")

try:

    lyrics = generate_lyrics(
        generator,
        genre,
        mood,
        topic
    )

    print("Generated Meyxana:\n")

    print(lyrics)

except Exception as e:

    logger.error(f"Generation Error: {e}")