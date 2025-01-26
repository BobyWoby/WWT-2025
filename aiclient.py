from  openai import OpenAI

client = OpenAI()

email = "2025.kzheng@jburroughs.org"

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
            a suspicious email from {email}
            """
        }
    ]
)