
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai

openai.api_key = "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"

app = FastAPI()

# اجازه دسترسی از همه دامین‌ها (برای ارتباط با frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/diagnose")
async def diagnose_issue(request: Request):
    data = await request.json()
    issue = data.get("issue", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a bilingual aircraft maintenance assistant trained on Boeing 737-400 AMM and WDM. Respond in both English and Persian."},
            {"role": "user", "content": issue}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return {"response": reply}
