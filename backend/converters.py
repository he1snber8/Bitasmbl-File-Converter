# conversion helpers (use PyPDF2 / Pillow)
from PIL import Image
from PyPDF2 import PdfReader

def pdf_to_text(path) -> str:
    # TODO: implement PDF text extraction
    reader = PdfReader(path)
    return "\n".join(p.extract_text() or "" for p in reader.pages)

def image_to_png(in_path, out_path):
    # convert images to PNG
    Image.open(in_path).save(out_path, "PNG")
