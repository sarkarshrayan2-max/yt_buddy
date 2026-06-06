from src.transcript import get_transcript
from src.summarizer import summarize_video

url = "https://www.youtube.com/watch?v=RwlgFC6S-OE&t=149s"

data = get_transcript(url)

summary, processing_info = summarize_video(data["transcript"])

print("\nProcessing Info:")
print(processing_info)

print("\nSummary:\n")
print(summary)