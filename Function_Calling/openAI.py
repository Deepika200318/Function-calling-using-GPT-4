import os
import re

# from dateutil import parser as date_parser

from openai import OpenAI


from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema,StructuredOutputParser
from dotenv import load_dotenv

load_dotenv()

# Access the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

from response_schema import (
    user_id,
    transaction_id
    # password
)
# print("Type of user id",(user_id))
id_field = ResponseSchema(name="userID", description=str(user_id))
transaction_field = ResponseSchema(name="transactionID", description=str(transaction_id))
# password_field = ResponseSchema(name="password", description=password)

# schema with all entities (fields) to be extracted
conversation_metadata_output_schema_parser = StructuredOutputParser.from_response_schemas(
    [      
        id_field,
        transaction_field
    ]
)

conversation_metadata_output_schema=conversation_metadata_output_schema_parser.get_format_instructions()
# print(conversation_metadata_output_schema)

conversation_metadata_prompt_template_str = """
Given an input query by the user, which contains the details of the user id and transaction id. Make relational mapping for user id with correct user id and transaction id with correct
transaction id. For example, if the input string is like "my user id is 324562678", the user id is mapped to 324562678. Map it accordingly. And if the input string is like 
"My transaction is is 1234567", the transaction id is mapped to 1234567. Extract the following metadata according to the format instructions below. If there is no user id provided, return null and if no 
transaction id provided, return null in its field. If the query that is sent is in the form of a function like get_status(89709), then consider 89709 as the userid.
If two arguments are passed, then consider the first argument is user id and second argument is transaction id.
 
<< FORMATTING >>
{format_instructions}
 
<< INPUT >>
{user_info}
 
<< OUTPUT (remember to include the ```json)>>"""
 
conversation_metadata_prompt_template = PromptTemplate.from_template(template=conversation_metadata_prompt_template_str)

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content

def usrid_extract(final_transcript: str):
    conversation_metadata_recognition_prompt = (
        conversation_metadata_prompt_template.format(
            user_info=final_transcript,
            format_instructions = conversation_metadata_output_schema
        )
    )
    conversation_metadata_detected_str = get_completion(conversation_metadata_recognition_prompt)
    # print(type(conversation_metadata_detected_str))
    # print("JSON String:", conversation_metadata_detected_str)  # Print JSON string for debugging
    return conversation_metadata_detected_str
   
# query = "My user id is 546327. My password is abc"
# k=usrid_extract(query)
# print(k)