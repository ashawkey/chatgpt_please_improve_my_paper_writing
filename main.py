from revChatGPT.V1 import Chatbot
import gradio as gr
import json

print(f'[INFO] Loading Config...')
with open('config.json', 'r') as f:
    config = json.load(f)
print(config)

print(f'[INFO] Initializing Chatbot API...')
chatbot = Chatbot(config=config)

def submit(x):
    for data in chatbot.ask(x):
        message = data["message"]
    return message

print(f'[INFO] Warming up chatgpt to behave as an English writing improver...')

init_prompt = """
I would like to engage your services as an academic writing consultant to improve my writing. 
I will provide you with text that requires refinement, and you will enhance it with more academic language and sentence structures.
The essence of the text should remain unaltered, including any LaTeX commands. 
I request that you provide only the improved version of the text without any further explanations.
"""

response = submit(init_prompt)

print(f'[INFO] Warming up: \n{response}')

print(f'[INFO] Starting Gradio APP...')

with gr.Blocks() as app:
    gr.Markdown("### ChatGPT, please help to improve my paper writing!")
    
    with gr.Row():

        text_input = gr.Textbox(label="Input", lines=10)
        text_output = gr.Textbox(label="Output", lines=10)

    text_button = gr.Button("Submit")
    text_button.click(submit, inputs=text_input, outputs=text_output)

app.launch()