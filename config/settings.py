from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"