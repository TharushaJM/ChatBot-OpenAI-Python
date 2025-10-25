from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=OPENAI_API_KEY)


while True:
        
    question=input("User: ")
    if question != "Bye":
        
        response= client.chat.completions.create(
            model='gpt-4o' ,
            messages=[{"role": "user", "content": question}],
            max_tokens=50,
            n=1,      
            temperature=0  #response randomness 
            
        )
        for choice in response.choices:
            print(f"AI: {choice.message.content}")
    else:
        print('AI: Bye....')
        break