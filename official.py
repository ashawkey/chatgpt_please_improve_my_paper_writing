import gradio as gr
import json
import os
import openai
from prompt import *

print(f'[INFO] Loading API key from env...')

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print('[WARN] OPENAI_API_KEY key not found in env')

def submit(x, simple=False):
    # everytime we restart a new conversation.
    if simple:
        results = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": PREFIX_PROMPT + x},
            ]
        )
    else:    
        results = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": INIT_PROMPT},
                {"role": "user", "content": PREFIX_PROMPT + x},
            ]
        )
    total_tokens = results['usage']['total_tokens']
    cost = (total_tokens / 1000) * 0.002 # in dollar
    response = results['choices'][0]['message']['content']
    return response, cost

print(f'[INFO] Starting Gradio APP...')

with gr.Blocks() as app:
    gr.Markdown("### ChatGPT, please help to improve my paper writing!")

    # allow setting API key in gui
    with gr.Row():
        api_input = gr.Textbox(label="OPENAI_API_KEY", value=openai.api_key, lines=1)
        def save_api(x): openai.api_key = x
        api_input.change(save_api, api_input)

    simple_checkbox = gr.Checkbox(value=False, label='simple mode (only send the prefix prompt, 0.00142$ cheaper per query)')

    with gr.Row():

        text_input = gr.Textbox(label="Input", lines=10)

        with gr.Column():
            text_output = gr.Textbox(label="Output", lines=10)
            cost = gr.Number(label='cost of this query ($)')

    text_button = gr.Button("Submit")
    text_button.click(submit, inputs=[text_input, simple_checkbox], outputs=[text_output, cost])
    
app.launch()