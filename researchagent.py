import  os, json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                                   # reads .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("MODEL_NAME", "gpt-4o-mini")

SYSTEM_PROMPT = "You are Vision, a friendly AI research assistant. Use simple language."

def chat(history):
    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=history,          # the whole conversation
    )
    return response.output_text

def clean_json(text):
    text = text.strip()
    if text.startswith(""):
        text = text.split("\n", 1)[1].rsplit("", 1)[0]
    return text.strip()

def create_research_plan(topic):
    prompt = f"""Break this topic into 5 research questions: {topic}
Return ONLY JSON, no markdown:
{{"topic": "{topic}", "questions": ["q1","q2","q3","q4","q5"]}}"""
    response = client.responses.create(model=MODEL, input=prompt)
    return json.loads(clean_json(response.output_text))
