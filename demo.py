import openai
import os

openai.api_key=os.getenv('OPENAI_API_KEY')

def getAIsay(textfromg):
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt="tldr zhtw\n".join(textfromg),
        max_tokens=128,
        temperature=0.5,
    )
    return res["choices"][0]["text"]

if __name__ == "__main__":
    print(getAIsay("Sth"))