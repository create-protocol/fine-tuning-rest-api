import os
from together import Together

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

response = client.images.generate(
    prompt="space robots",
    model="stabilityai/stable-diffusion-xl-base-1.0",
    steps=10,
    n=4,
)
print(response.data[0].b64_json)