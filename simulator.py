from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key = api_key,
)


user_input  = input("Ask Anything : ")
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": user_input},
    {"role": "system", "content": "You are a helpful assistant."}
  ]
)


print("assistant’s reply :",completion.choices[0].message.content)
print("token usage: ", completion.usage.total_tokens)

