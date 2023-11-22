from openai import OpenAI

API_KEY = #insert your API key here

client = OpenAI(
    api_key=API_KEY
)

messages = []
bot_role = input("What kind of virtual assistant would you like? >> ")
messages.append({"role": "system", "content": bot_role})

print("Virtual assistant successfully created!")

while True:
    gptMessage = input("Prompt your VA (or type QUIT) >> ")
    messages.append({"role": "user", "content": gptMessage})

    if gptMessage.lower != "quit":
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print("\n" + reply + "\n")
    else:
        break
