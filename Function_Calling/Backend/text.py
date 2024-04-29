import os
from openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
# from chatgpt import response_generate

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Check if the API key is available
if api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")
# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

conversation_metadata_prompt_template_str = """
Based on the user query  - {user_query} and the information gathered from the function call - {func_op}. Analayse the user query and respective function output and generate the response.
"""
# If the {func_op} is null, then ask the user to provide his/her userid to provide the required information according to the {user_query}

conversation_metadata_prompt_template = PromptTemplate.from_template(template=conversation_metadata_prompt_template_str)
def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content

def response_generate(input_text: str,function_op: str):
    conversation_metadata_recognition_prompt = (
        conversation_metadata_prompt_template.format(
            user_query=input_text,
            func_op=function_op
        )
    )
    conversation_metadata_detected_str = get_completion(conversation_metadata_recognition_prompt)

    return conversation_metadata_detected_str  
