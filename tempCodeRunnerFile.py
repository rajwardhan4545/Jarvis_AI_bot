def ai(prompt):
#     client = OpenAI(api_key=apikey)
#     text=f"OpenAI response for Prompt : {prompt} \n ****************************\n\n"
#     response = client.completions.create(
#         model="gpt-3.5-turbo-instruct",
#         prompt=prompt,
#         temperature=1,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # print(response.choices[0].text)
#     text+=response.choices[0].text
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")
#     with open(f"Openai/{''.join(prompt.split('write')[1:])}.txt","w") as f:
#         f.write(text)
#         f.write(response.choices[0].text)