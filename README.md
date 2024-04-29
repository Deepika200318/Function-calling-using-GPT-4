# fetch-data
An interactive chat bot, which uses function calling to call the custom API from chatgpt, and displays the data returned by the API to the user.
## Server
A Server is created, through which API endpoints are made. These API's are called when the respective custom function is called.
Start the server using the command ``` uvicorn server:app --reload --port 8077 --host 0.0.0.0 ``` 
### Working
An assistant is made. We use function calling tool here.

 _The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and files to respond to user queries. The Assistants API currently supports three types of tools: Code Interpreter, File Search, and Function calling.

Assistant is provided with all the custom functions and their descriptions in tool section. The assistant decides if the custom functions need to be called or not. If needed, which function to call, based on the description of the custom functions.

A thread is created for the assistant.

 _A Thread represents a conversation between a user and one or many Assistants. You can create a Thread when a user (or your AI application) starts a conversation with your Assistant.

 A run is created for the thread, which is responsible to run the thread.
