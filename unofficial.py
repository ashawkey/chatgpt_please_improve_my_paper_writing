from revChatGPT.V1 import Chatbot
import gradio as gr
import json

INIT_PROMPT = """I would like to engage your services as an academic writing consultant to improve my writing. 
I will provide you with text that requires refinement, and you will enhance it with more academic language and sentence structures.
The essence of the text should remain unaltered, including any LaTeX commands. 
I request that you provide only the improved version of the text without any further explanations."""

PREFIX_PROMPT = "Please refine the following text in academic English: \n"

print(f'[INFO] Loading Config...')
with open('config.json', 'r') as f:
    config = json.load(f)
print(config)

print(f'[INFO] Initializing Chatbot API...')
chatbot = Chatbot(config=config)

def reset():
    print(f'[INFO] reset chatting...')
    chatbot.reset_chat()
    response = submit(INIT_PROMPT, prefix='')
    print(f'[INFO] resetting response: \n{response}')
    return "" # empty textbox

def regen(x):
    print(f'[INFO] rollback and regenerate.')
    chatbot.rollback_conversation(1)
    return submit(x)

def submit(x, prefix=PREFIX_PROMPT):
    for data in chatbot.ask(prefix + x):
        message = data["message"]
    return message

print(f'[INFO] Warming up chatgpt to behave as an English writing improver...')

response = submit(INIT_PROMPT, prefix='')

print(f'[INFO] Warming up: \n{response}')

print(f'[INFO] Starting Gradio APP...')

with gr.Blocks() as app:
    gr.Markdown("### ChatGPT, please help to improve my paper writing!")

    reset_button = gr.Button("Reset chat when something is off.")
    
    with gr.Row():

        text_input = gr.Textbox(label="Input", lines=10)
        text_output = gr.Textbox(label="Output", lines=10)

    with gr.Row():
        text_button = gr.Button("Submit")
        regen_button = gr.Button("Regenerate")
    
    reset_button.click(reset, outputs=text_output)
    text_button.click(submit, inputs=text_input, outputs=text_output)
    regen_button.click(regen, inputs=text_input, outputs=text_output)

app.launch()