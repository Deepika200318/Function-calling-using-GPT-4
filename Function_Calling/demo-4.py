# chainlit run demo-4.py -w
from dotenv import load_dotenv
import os
from openai import OpenAI
from openai import ChatCompletion
import json
import requests
from openAI import usrid_extract
from langchain.prompts import PromptTemplate
from text import response_generate
import chainlit as cl

load_dotenv()

# Access the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

GPT_MODEL = "gpt-4-turbo"
client = OpenAI()

# For fetching the balance
def func_call(query: str):
    # Extract the user id here.
    txt = usrid_extract(query)
    print("I am the query given to function call: ",query)
    txt = txt.strip().strip('`').strip()
    lines = txt.strip().split('\n', 1)
    if len(lines) > 1:
        txt = lines[1].strip()
    print("dECODED Text: ",txt)

    if(txt[0]== "null"):
        return None

    data= json.loads(txt)
    usr_id = data["userID"]
    print("This is user id: ", usr_id)
    if(usr_id==None):
        return usr_id
    print("This is data: ", data)
    result = call_api(data)
    print((result))
    x = json.dumps(result)
    return x

def call_api(usr_id):

    if usr_id is None:
        print("Userid not found in the database.")
        return None
    try:
        url = "http://3.7.80.204:8077/balance/"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=usr_id, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to call API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# For fetching the address
def func_call_address(query: str):
    # Extract the user id here.
    txt = usrid_extract(query)
    print("I am the query given to function call: ",query)
    txt = txt.strip().strip('`').strip()
    lines = txt.strip().split('\n', 1)
    if len(lines) > 1:
        txt = lines[1].strip()
    print("dECODED Text: ",txt)

    if(txt[0]== "null"):
        return None
    print("I am the text type: ",type(txt))

    data= json.loads(txt)
    usr_id = data["userID"]
    print("This is user id: ", usr_id)
    if(usr_id==None):
        return usr_id
    print("This is data: ", data)
    result = call_api_address(data)
    print((result))
    x = json.dumps(result)
    return x

def call_api_address(usr_id):

    if usr_id is None:
        print("Userid not found in the database.")
        return None
    try:
        url = "http://3.7.80.204:8077/address/"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=usr_id, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to call API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# For fetching the name
def func_call_name(query: str):
    # Extract the user id here.
    txt = usrid_extract(query)
    print("I am the query given to function call: ",query)
    txt = txt.strip().strip('`').strip()
    lines = txt.strip().split('\n', 1)
    if len(lines) > 1:
        txt = lines[1].strip()
    print("dECODED Text: ",txt)

    if(txt[0]== "null"):
      return None

    data= json.loads(txt)
    usr_id = data["userID"]
    print("This is user id: ", usr_id)
    if(usr_id==None):
        return usr_id
    print("This is data: ", data)
    result = call_api_name(data)
    print((result))
    x = json.dumps(result)
    return x

def call_api_name(usr_id):

    if usr_id is None:
        print("Userid not found in the database.")
        return None
    try:
        url = "http://3.7.80.204:8077/name/"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=usr_id, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to call API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

# For fetching the Payment status
def func_call_payment(query: str):
    # Extract the user id here.
    print("I am the query given to function call: ",query)
    txt = usrid_extract(query)
    print("I am called by the function call")
    txt = txt.strip().strip('`').strip()
    lines = txt.strip().split('\n', 1)
    if len(lines) > 1:
        txt = lines[1].strip()
    print("dECODED Text: ",txt)

    if(txt[0]== "null"):
        return None

    data= json.loads(txt)
    usr_id = data["userID"]
    print("This is user id: ", usr_id)
    if(usr_id==None):
        return usr_id
    print("This is data: ", data)
    result = call_api_payment(data)
    print((result))
    x = json.dumps(result)
    return x

def call_api_payment(usr_id):

    if usr_id is None:
        print("Userid not found in the database.")
        return None
    try:
        url = "http://3.7.80.204:8077/paymentStatus/"
        headers = {'Content-Type': 'application/json'}
        print("I am the type of data being sent to the api call", type(usr_id))
        response = requests.get(url, json=usr_id, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to call API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# Getting Transaction status
def func_call_transaction(query: str):
    # Extract the user id here.
    print("I am the query given to function call: ",query)
    txt = usrid_extract(query)
    print("I am called by the function call")
    txt = txt.strip().strip('`').strip()
    lines = txt.strip().split('\n', 1)
    if len(lines) > 1:
        txt = lines[1].strip()
    print("dECODED Text: ",txt)

    if(txt[0]== "null"):
        return None
    
    if(txt[1] =="null"):
        txn_id = None
        x = json.dumps(txn_id)
        return x

    data = json.loads(txt)
    usr_id = data["userID"]
    txn_id = data["transactionID"]
    print("This is user id: ", usr_id)
    print("This is the transaction id", txn_id)
    if(usr_id==None):
        return usr_id
    print("This is data: ", data)
    result = call_api_transaction(data)
    print((result))
    x = json.dumps(result)
    return x

def call_api_transaction(usr_id):

    if usr_id is None:
        print("Userid not found in the database.")
        return None
    try:
        url = "http://3.7.80.204:8077/transactionStatus/"
        headers = {'Content-Type': 'application/json'}
        print(type(usr_id))
        response = requests.get(url, json=usr_id, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to call API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def get_completion(prompt, model= "gpt-4-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0.2)
    # Check the token usage
    print(f"Token usage: {response.usage}")
    return response.choices[0].message.content

def create_assistant_and_process_query(query, history):

    # chat_history = history
  # prompt_template = """You are a Banking bot. You are designed to answer some financial questions. You will be asked with five types of questions about the user's name, bank balance, address, transaction status and payment status. 
  # Decide which function to call, to answer the user's queries. Also, you will be provided with the user query history. Go through it and if there is some query,
  # which is relavent to some function, then call that function. If user id is provided in the chat history, then send the user id also while calling the function. If there is no user id provided in the user query and still if the function is to be called, then ask the user to provide the user id.
  # Here is the conversational history between the user and the chatbot. If the user provides the userid in that message, then check in the chat history if he/she is asking to provide some information. If found, get them that information accordingly by making proper function calls.
  # Else, If you did not find anything as such in the chat history, then ask the user what does he/she wants to know. If the user id is already provided in the chat history, then add the user id along with the query.
  # <history>
  # {chat_history}
  # </history>
  # """

 
  # append that information in the query and send the query to function call.
  # Example:
  # If the decided functin call is "check_transaction_status(user_id=1079, transaction_id=755)", then send the query as "check_transaction_status(user_id=1079, transaction_id=755)
  # to the function to be called. If the final prompt is "Based on the conversation history, the user has provided their user id (4321564) and has asked for their address. Therefore, the function to call would be `get_address(user_id)`.",
  # then the query sent to the function call should be get_address(4321564).

  #  It need not be a compulsion
  # to make a function call. only make the function call if the input query requires to call it. if not required, generate the response that can be shown to the user.
  # The query that is being sent to the function must be clear with its instructions. For example, if there is some user id, appened some thing like user id is xxxxx to the query that is passed to the function call. 

  # complete_prompt= get_completion(prompt)

  # print("I am the prompt: ", complete_prompt)

  complete_prompt= get_usr_query(query,history)
  print("This is the generated prompt: ", complete_prompt)

  query = query+". "+complete_prompt

  assistant = client.beta.assistants.create(
    name = "Freo customer service",
    description= """This is the assistant meant to answer financial related questions. 
    You will have to decide when to call a function. Some functions require user id and transaction id as arguments. So if you dont have them then ask the user to provide it.
    """,
    # instructions="""You are a Banking bot. You are designed to answer some financial questions. You will be asked with three types of questions - what is my bank balance, what is my name and what is my address. 
    # Decide which function to call, to answer the user's queries. Also, you will be provided with the user query history. Go through it and if there is some query,
    # which is relavent to some function, then call that function. If there is no user id provided in the user query and still if the function is to be called, then ask the user to provide the user id.
    # Here is the conversational history between the user and the chatbot.
    # <history>
    # {chat_history}
    # </history>
    # """,
    instructions = complete_prompt,
    # instructions = ""
    model = "gpt-4-turbo", 
    tools= [
        {
            # for balance
          "type": "function",
          "function": {
            'name' : 'func_call',
            'description' : 'Gets the bank balance of the required user only if the user id is available',
            "parameters": {
              "type": "object",
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The query or message sent by the user",
                },
              },
              "required": ["query"],
            },
          }  
        },
        {
          "type": "function",
          "function": {
            'name' : 'func_call_address',
            'description' : 'Gets the address of the required user corresponding to the user id.',
            "parameters": {
              "type": "object",
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The query or message sent by the user",
                },
              },
              "required": ["query"],
            },
          }  
        },
        {
          "type": "function",
          "function": {
            'name' : 'func_call_name',
            'description' : 'Gets the name of the required user corresponding to the user id.',
            "parameters": {
              "type": "object",
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The query or message sent by the user",
                },
              },
              "required": ["query"],
            },
          }  
        },
        {
          "type": "function",
          "function": {
            'name' : 'func_call_transaction',
            'description' : 'Gets the transaction status of the queried transaction id required user corresponding to the user id and transaction id.',
            "parameters": {
              "type": "object",
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The query or message sent by the user",
                },
              },
              "required": ["query"],
            },
          }  
        },
        {
          "type": "function",
          "function": {
            'name' : 'func_call_payment',
            'description' : 'Gets the payment status of the required user corresponding to the user id.',
            "parameters": {
              "type": "object",
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The query or message sent by the user",
                },
              },
              "required": ["query"],
            },
          }  
        },
    ]
  )

  print("Assistant created!")
  
  thread = client.beta.threads.create()
  print("Creating a thread...")

  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content = query
  )
  print("Adding message to thread")

  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
  )
  print("Run created")


  # Wait for the run to complete
  while run.status in ['queued', 'in_progress']:
    print("Status of the run: ",run.status)
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Retrieve and print the messages from the thread
    messages = client.beta.threads.messages.list(thread_id=thread.id)

  if run.status == 'requires_action':
    # Extract information about the required action
    tool_calls = run.required_action.submit_tool_outputs.tool_calls
    
    # Iterate over the tool calls
    for tool_call in tool_calls:
        # Extract information about the function call
        function_name = tool_call.function.name
        function_arguments = tool_call.function.arguments
        available_functions = {
          "func_call" : func_call,
          "func_call_address" : func_call_address,
          "func_call_name" : func_call_name,
          "func_call_payment" : func_call_payment,
          "func_call_transaction" : func_call_transaction

        }
        fuction_to_call = available_functions[function_name]
        print("I have to be called: ", fuction_to_call)
        print("We are the arguments if the given function: ", function_arguments)
        # Execute the function call
        function_arguments_dict = json.loads(function_arguments)
        output = fuction_to_call(*list(function_arguments_dict .values()))
        print("I am the output ",(output))
        # if(output==None)
        # Check if the output was successfully submitted
        print("I am the actual query: ", query)
        reply = response_generate(query,output)
        print("I am produced by the response generate code: ",reply)
        return reply

  if run.status == 'completed': 
    print("Run status: ",run.status)
    messages = client.beta.threads.messages.list(
      thread_id=thread.id
    )
    print("Message getting printed after the run is completed: ",messages.data[0].content[0].text.value)
    return (messages.data[0].content[0].text.value)

# u_query = "Who is the president of India?"
# a=create_assistant_and_process_query(query=u_query)
# print(type(a))

def get_usr_query(usr_msg,history):
     # chat_history = history
  prompt_template = """
  You are a Chat bot. You have special ability to answer some financial questions using function calling. 
  There are five types of questions which include the user's name, bank balance, address, transaction status and the payment status. Decide which function to call.

  Your work is to modify the {user_query}, to be sent to the function by including the user id and transaction id, if provided in the chat history and send to the function.
  
  You will be provided with the chat history.
  If there is no user id provided in the user query and still if the function is to be called, then ask the user to provide the user id. 
  If the user asks for the transaction status and if any of the user id or transaction id is missing, ask the user to provide the required one. 

  If the user provides the userid in that message, then check in the chat history if user is asking to provide some information. If found, get them that information accordingly by making proper function calls.
  Else, ask what does the user want.

  Here is the conversational history between the user and the chatbot. Don't hallucinate. Just answer the questions asked by the user.
  <history>
  {chat_history}
  </history>
  Example:
  If the decided functin call is "check_transaction_status(user_id=1079, transaction_id=755)", then send the query as "check_transaction_status(user_id=1079, transaction_id=755)
  to the function to be called. If the final prompt is "Based on the conversation history, the user has provided their user id (4321564) and has asked for their address. Therefore, the function to call would be `get_address(user_id)`.",
  then the query sent to the function call should be get_address(4321564).
  """

  generate_prompt= PromptTemplate.from_template(template=prompt_template)

  prompt = generate_prompt.format(
    # chat_history="\n".join([f"{speaker}: {message}" for speaker, message in history]),
    chat_history=history,
    user_query=usr_msg
  )
  complete_prompt= get_completion(prompt)
  print("I am the generated user query: ", complete_prompt)
  return complete_prompt



history=[]
history.append("Hi, Welcome to your Personalised Customer Support Bot. How can I help you today?")

@cl.on_chat_start
async def start():
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to your Personalised Customer Support Bot. How can I help you today?"
    await msg.update()
@cl.on_message
async def on_message(usr_qry: cl.Message):
    history.append(usr_qry.content)
    # reply = create_assistant_and_process_query(usr_qry.content,history)

    reply = create_assistant_and_process_query(usr_qry.content,history)
    history.append(reply)
    await cl.Message(content=reply).send()


# run = client.beta.threads.runs.submit_tool_outputs(
#   thread_id=thread.id,
#   run_id=run.id,
#   tool_outputs=[
#       {
#         "tool_call_id": call_ids[0],
#         "output": "22C",
#       },
#       {
#         "tool_call_id": call_ids[1],
#         "output": "LA",
#       },
#     ]
# )

#Handel the null cases ------------> When the user id is null