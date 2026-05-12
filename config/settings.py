from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

MODEL_NAME = "bigscience/bloom-560m"

MAX_NEW_TOKENS = 80

TEMPERATURE = 0.8

TOP_K = 40

TOP_P = 0.90

REPETITION_PENALTY = 1.2