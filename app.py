import streamlit as st

from src.transcript import get_transcript
from src.summarizer import summarize_video
from src.rag import create_vector_store, answer_question
from src.pdf_generator import generate_pdf

st.set_page_config(
    page_title="YT Buddy",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YT Buddy")
st.subheader("AI YouTube Summarizer & Video Chat")
st.write("Paste a YouTube URL, summarize the video, and chat with its content.")


# ---------------- SESSION STATE ----------------

if "summary" not in st.session_state:
    st.session_state.summary = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "processing_info" not in st.session_state:
    st.session_state.processing_info = None

if "video_data" not in st.session_state:
    st.session_state.video_data = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_url" not in st.session_state:
    st.session_state.current_url = None


# ---------------- INPUT SECTION ----------------

url = st.text_input("Enter YouTube URL")

col_a, col_b = st.columns([1, 1])

with col_a:
    generate_btn = st.button("Generate Summary", use_container_width=True)

with col_b:
    clear_btn = st.button("Clear Session", use_container_width=True)


if clear_btn:
    st.session_state.summary = None
    st.session_state.vector_store = None
    st.session_state.processing_info = None
    st.session_state.video_data = None
    st.session_state.chat_history = []
    st.session_state.current_url = None
    st.rerun()


# ---------------- GENERATE SUMMARY ----------------

if generate_btn:
    if not url:
        st.warning("Please enter a YouTube URL first.")

    else:
        try:
            with st.spinner("Extracting transcript, summarizing video, and building RAG index..."):
                video_data = get_transcript(url)

                summary, processing_info = summarize_video(
                    video_data["transcript"]
                )

                vector_store = create_vector_store(
                    video_data["transcript"]
                )

                st.session_state.video_data = video_data
                st.session_state.summary = summary
                st.session_state.processing_info = processing_info
                st.session_state.vector_store = vector_store
                st.session_state.chat_history = []
                st.session_state.current_url = url

            st.success("Summary generated successfully!")

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")


# ---------------- OUTPUT SECTION ----------------

if st.session_state.summary:

    st.divider()

    st.write("## 📌 Video Information")

    info = st.session_state.processing_info
    video_data = st.session_state.video_data

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Video ID", video_data["video_id"])

    with col2:
        st.metric("Word Count", info["word_count"])

    with col3:
        st.metric("Processing Mode", info["mode"])

    with col4:
        st.metric("Chunks Used", info["chunks_required"])

    st.caption(f"Current URL: {st.session_state.current_url}")

    st.divider()

    st.write("## 📝 Video Summary")

    with st.expander("View Full Summary", expanded=True):
        st.markdown(st.session_state.summary)

    st.divider()

    # ---------------- CHAT SECTION ----------------

    st.write("## 💬 Chat With Video")

    st.info(
        "Ask questions based on the video transcript. "
        "The answer will be generated using retrieved transcript chunks."
    )

    question = st.text_input("Ask a question about the video")

    ask_btn = st.button("Ask Question", use_container_width=True)

    if ask_btn:
        if not question:
            st.warning("Please enter a question.")

        elif st.session_state.vector_store is None:
            st.warning("Please generate a summary first.")

        else:
            try:
                with st.spinner("Searching transcript and generating answer..."):
                    answer = answer_question(
                        st.session_state.vector_store,
                        question
                    )

                    st.session_state.chat_history.append(
                        {
                            "question": question,
                            "answer": answer
                        }
                    )

            except Exception as e:
                st.error(f"Question answering failed: {str(e)}")

    if st.session_state.chat_history:
        st.write("### Chat History")

        for chat in reversed(st.session_state.chat_history):
            with st.chat_message("user"):
                st.markdown(chat["question"])

            with st.chat_message("assistant"):
                st.markdown(chat["answer"])
    st.divider()
    #-----------PDF GENERATION----------------
    st.write("## 📄 Export PDF")

    if st.button("Generate PDF", use_container_width=True):
        pdf_path = generate_pdf(
            video_url=st.session_state.current_url,
            summary=st.session_state.summary,
            chat_history=st.session_state.chat_history
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Download PDF Summary",
                data=pdf_file,
                file_name="yt_buddy_summary.pdf",
                mime="application/pdf",
                use_container_width=True
            )