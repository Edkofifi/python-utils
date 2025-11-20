from pypdf import PdfReader, PdfWriter

def replace_page(input_pdf, replacement_pdf, output_pdf, page_number):
    """
    page_number is 1-based index
    """
    reader = PdfReader(input_pdf)
    replace_reader = PdfReader(replacement_pdf)
    writer = PdfWriter()

    # Convert page_number → zero-based
    index = page_number - 1

    for i, page in enumerate(reader.pages):
        if i == index:
            # Insert replacement page instead of original
            writer.add_page(replace_reader.pages[0])
        else:
            writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

replace_page(
    "original.pdf",
    "resume.pdf",
    "output.pdf",
    1  # Replace page 1
)
