import easyocr
from PIL import Image
import numpy as np

# ------------------------------------------------ #
# Load EasyOCR Model (only once)
# ------------------------------------------------ #

reader = easyocr.Reader(
    ['en'],
    gpu=False
)


# ------------------------------------------------ #
# Extract Text from Image
# ------------------------------------------------ #

def extract_text_from_image(uploaded_file):
    """
    Extracts text from an uploaded image using EasyOCR.

    Parameters
    ----------
    uploaded_file : UploadedFile
        Image uploaded from Streamlit.

    Returns
    -------
    str
        Extracted text.
    """

    # Open image
    image = Image.open(uploaded_file)

    # Convert to RGB
    image = image.convert("RGB")

    # Convert PIL Image to NumPy array
    image_np = np.array(image)

    # OCR
    results = reader.readtext(
        image_np,
        detail=0,
        paragraph=True
    )

    # Combine detected text
    extracted_text = "\n".join(results)

    return extracted_text