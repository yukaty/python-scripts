import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load the API key from .env
load_dotenv('.env', override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Generate an image
response = client.images.generate(
  model="dall-e-2",
  prompt="An adorable baby seal with fluffy white fur, eating authentic Japanese sushi",
  size="512x512",
  quality="standard",
  n=1,
)

# Download the image
image_url = response.data[0].url
image_response = requests.get(image_url)

# Get the current timestamp for the filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
image_path = f"generated_image_{timestamp}.png"

# Save the image
if image_response.status_code == 200:
  with open(image_path, 'wb') as f:
    f.write(image_response.content)
    print(f"Image saved as {image_path}")
else:
  print(f"Failed to download image: {image_response.status_code} {image_response.content}")
