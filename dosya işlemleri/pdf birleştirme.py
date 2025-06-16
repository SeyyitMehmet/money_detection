import PyPDF2
import os


def merge_pdfs(pdf_paths, output_pdf_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path in pdf_paths:
        pdf_reader = PyPDF2.PdfReader(pdf_path)

        # Append each page of the PDF to the writer
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # Write out the merged PDF
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)


def get_pdfs_from_directory(directory_path):
    # Get a list of all PDF files in the directory
    pdf_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.lower().endswith('.pdf')]
    return pdf_files


# Directory containing PDF files
input_directory = 'C:/Users/sms/Desktop/belgelerim/pdfs/birleştirilecek'  # Replace with your directory path
output_pdf_path = 'C:/Users/sms/Desktop/belgelerim/merged_output2.pdf'  # Replace with your output PDF path

pdf_paths = get_pdfs_from_directory(input_directory)

merge_pdfs(pdf_paths, output_pdf_path)
