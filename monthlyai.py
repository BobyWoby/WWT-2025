from openai import OpenAI

client = OpenAI()

completion = client.complete.create(
    model: "gpt-4o-mini",
    messages: [
        {
            "role": "developer", "content": "You are writing a phishing email to a John Burroughs teacher." #int
        },
        {
            "role": "user", "content": "Write a phishing email directed towards highschool faculty" # what you would put in ChatGPT chat box 
        },
    ],
    
)
print(completion.choices[0].message)