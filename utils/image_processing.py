from PIL import Image
import io

def preprocess_image(file_content: bytes) -> bytes:
    """Preprocess the image before sending to the model."""
    try:
        image = Image.open(io.BytesIO(file_content))
        return file_content
    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")