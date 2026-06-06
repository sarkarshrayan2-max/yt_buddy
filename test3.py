from src.transcript import get_transcript
from src.rag import create_vector_store, answer_question

url = "https://www.youtube.com/watch?v=RwlgFC6S-OE&t=149s"

data = get_transcript(url)

vector_store = create_vector_store(data["transcript"])

while True:
    question = input("\nAsk a question: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = answer_question(vector_store, question)

    print("\nAnswer:")
    print(answer)