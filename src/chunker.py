def count_words(text):
    return len(text.split())


def split_transcript(transcript, chunk_size=3000, overlap=300):
    words = transcript.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size

        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        start = end - overlap

    return chunks


def get_processing_mode(transcript, threshold=5000):
    word_count = count_words(transcript)

    if word_count <= threshold:
        return {
            "mode": "direct",
            "word_count": word_count,
            "chunks_required": 1
        }

    chunks = split_transcript(transcript)

    return {
        "mode": "chunked",
        "word_count": word_count,
        "chunks_required": len(chunks)
    }