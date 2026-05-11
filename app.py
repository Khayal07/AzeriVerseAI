from core.model_loader import load_generator
from core.generator import generate_lyrics

from utils.dataset_loader import load_dataset


print("Loading dataset...")

dataset = load_dataset("data/raw/meyxana.txt")

print("Dataset loaded successfully!")

print("\nDataset Preview")

print(dataset[:200])

print("\n----------------------\n")



print("Loading AI model...")

generator = load_generator()

print("Model loaded successfully!")


genre = "meyxana"
mood = "dark"
topic = "sevgi"

print("\nGenerating lyrics...\n")

lyrics = generate_lyrics(
    generator,
    genre,
    mood,
    topic
)

print(lyrics)