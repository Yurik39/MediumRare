import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
PRODUCT_URL = os.getenv("PRODUCT_URL")
CART_URL = os.getenv("CART_URL")