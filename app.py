from core.model_loader import load_generator
from core.generator import generate_lyrics


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