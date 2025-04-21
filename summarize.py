import os
import argparse
from transformers import pipeline
from docx import Document
import pdfplumber

def summarize_text(text, model_name="facebook/bart-large-cnn", max_length=130, min_length=30):
    summarizer = pipeline("summarization", model=model_name)
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

def read_txt_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf_file(file_path):
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def read_docx_file(file_path):
    doc = Document(file_path)
    return "\n".join(para.text for para in doc.paragraphs)

def get_file_contents(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        return read_txt_file(file_path)
    elif ext == ".pdf":
        return read_pdf_file(file_path)
    elif ext == ".docx":
        return read_docx_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def write_summary_to_file(summary, input_path):
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    out_path = f"summary_{base_name}.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary)
    return out_path

def main():
    parser = argparse.ArgumentParser(description="Summarize text from .txt, .pdf, or .docx files.")
    parser.add_argument("file", help="Path to the file to summarize.")
    parser.add_argument("--model", default="facebook/bart-large-cnn", help="Hugging Face summarization model.")
    parser.add_argument("--max_length", type=int, default=130, help="Maximum length of the summary.")
    parser.add_argument("--min_length", type=int, default=30, help="Minimum length of the summary.")
    args = parser.parse_args()

    try:
        input_text = get_file_contents(args.file)
        if not input_text.strip():
            raise ValueError("The file appears to be empty or unreadable.")
        
        print("Generating summary...")
        summary = summarize_text(input_text, args.model, args.max_length, args.min_length)
        output_path = write_summary_to_file(summary, args.file)
        print(f"\nSummary written to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    #python summarize.py filename.extension --model MODEL --max_length --min_length
    
