from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    """
    Merge multiple PDF files in a specific order.

    Args:
        pdf_list (list): List of PDF file paths in the desired merge order.
        output_filename (str): Name of the final merged PDF file.
    """
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
        print(f"Added: {pdf}")

    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF created successfully: {output_filename}")


if __name__ == "__main__": 
    pdf_files = [
        "Transcript_Diploma.pdf",
        "Certificate_Education.pdf",
    ]

    output_file = "merged_document.pdf"

    merge_pdfs(pdf_files, output_file)
