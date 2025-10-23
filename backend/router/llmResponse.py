from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


client = Groq()


# Function to handle LLM response
def handle_llm_response(message):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": message}],
        temperature=1.11,
        max_completion_tokens=38971,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None,
        tools=[{"type": "browser_search"}, {"type": "code_interpreter"}],
    )
    return completion.choices[0].message
