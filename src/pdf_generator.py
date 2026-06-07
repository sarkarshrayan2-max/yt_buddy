from fpdf import FPDF
import tempfile


def clean_text(text):
    return text.encode("latin-1", "replace").decode("latin-1")


def generate_pdf(video_url, summary, chat_history):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "YT Buddy - Video Summary", ln=True)

    pdf.ln(8)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Video URL:", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, clean_text(video_url))

    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Summary", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, clean_text(summary))

    if chat_history:
        pdf.ln(5)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Chat History", ln=True)

        for chat in chat_history:
            pdf.set_font("Arial", "B", 11)
            pdf.multi_cell(0, 8, clean_text(f"Question: {chat['question']}"))

            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8, clean_text(f"Answer: {chat['answer']}"))

            pdf.ln(4)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)

    return temp_file.name