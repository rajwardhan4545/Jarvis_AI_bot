
from config import apikey
from openai import OpenAI

client = OpenAI(api_key=apikey)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write an email to my boss for resignation/n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].text)

