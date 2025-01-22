import ollama
from config.settings import MODEL_CONFIG

def analyze_invoice(file_content: bytes) -> str:
    """Analyze invoice using the vision model."""
    try:
        return ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': MODEL_CONFIG['prompt'],
                'images': [file_content]
            }]
        ).message.content
    except Exception as e:
        if "connection was forcibly closed" in str(e):
            raise ValueError("Please ensure Ollama is running locally")
        raise ValueError(f"Error analyzing invoice: {str(e)}")