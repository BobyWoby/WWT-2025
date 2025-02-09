from  openai import OpenAI

email = "2025.kzheng@jburroughs.org"
client = OpenAI()

def hackedEmailPrompt(email, recipient):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "developer",
            "content": """You are writing an email to inform
            somebody that they were sent an email from a suspicious sender. 
            """
        },
        {
            "role": "user",
            "content": f"""
            write an email that tells the user that they have received 
            a suspicious email from {email}, address the email to {recipient}, and have it be sent from the sAIf gmail add-on
            """
        }
        ]
    )
    return completion