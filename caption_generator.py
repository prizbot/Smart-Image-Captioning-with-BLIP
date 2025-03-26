import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

# Specify local model path
model_path = r"C:\Users\2022PECAI179\Downloads\miniproject\miniproject\models\blip-image-captioning-large"

# Load model from local path
processor = BlipProcessor.from_pretrained(model_path)
model = BlipForConditionalGeneration.from_pretrained(model_path)

def generate_caption(image_bytes):
    """
    Generates a caption for the given image.
    
    Args:
        image_bytes (BytesIO): Image in bytes format.
    
    Returns:
        str: Generated caption.
    """
    try:
        # Convert bytes to PIL image
        image = Image.open(io.BytesIO(image_bytes.getvalue())).convert("RGB")

        # Process image
        inputs = processor(images=image, return_tensors="pt")

        # Generate caption
        caption_ids = model.generate(**inputs)
        caption = processor.batch_decode(caption_ids, skip_special_tokens=True)[0]

        return caption
    
    except Exception as e:
        return f"Error generating caption: {str(e)}"
