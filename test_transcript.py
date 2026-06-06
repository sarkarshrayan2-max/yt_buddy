from src.transcript import get_transcript
from src.summarizer import summarize_video

url = "https://www.youtube.com/watch?v=RgV57kDzcng&t=1s"

data = get_transcript(url)

summary = summarize_video(
    data["transcript"]
)

print(summary)