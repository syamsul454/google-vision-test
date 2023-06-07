# chat gpt api
import openai

def chat_gpt(q):
    openai.api_key = "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"
    pertanyaan = "Q: cara mengatasi orang" + q + "?\nA:"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=pertanyaan,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
    )
    return response["choices"][0]["text"]
