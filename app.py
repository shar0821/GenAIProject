import Flask

app =Flask(__name__)

!pip install transformers pillow torch  # Install required libraries if not already installed

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import requests
import torch

# 1. Load the model and corresponding processor (image feature extractor + tokenizer)
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def generate_caption(image_url: str) -> str:
    """
    Given an image URL, downloads the image and generates a caption.
    """
    # 2. Download and open the image
    response = requests.get(image_url)
    image = Image.open(response.raw).convert("RGB")

    # 3. Preprocess the image
    pixel_values = feature_extractor(image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    # 4. Generate caption
    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return caption

# Example usage
if __name__ == "__main__":
    # Try a sample image URL
    sample_image_url = "https://huggingface.co/datasets/hf-internal-testing/fixtures_image_utils/resolve/main/flower.png"

    caption = generate_caption(sample_image_url)
    print("Generated caption:", caption)


@app.route("/")
def hello_world()-> str:
    return "<p>Hello World</p>"

def dummy()-> str:
    print("Hello World")

if __name__ == "__main__":
    dummy()