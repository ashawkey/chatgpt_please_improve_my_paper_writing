import gradio as gr
import json
import os
import openai
from prompt import *

print(f'[INFO] Loading API key from env...')

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print('[WARN] OPENAI_API_KEY key not found in env')

def submit(x, api, init_prompt, prefix_prompt, temperature, simple=False):
    # reset api key everytime, so it won't save api unsafely...?
    openai.api_key = api 
    # restart a new conversation.
    if simple:
        results = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            temperature=temperature,
            messages=[
                {"role": "user", "content": prefix_prompt + x.strip()},
            ]
        )
    else:    
        results = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            temperature=temperature,
            messages=[
                # chatgpt doesn't pay much attention to system content.
                {"role": "user", "content": init_prompt + prefix_prompt + x.strip()},
            ]
        )
    total_tokens = results['usage']['total_tokens']
    cost = (total_tokens / 1000) * 0.002 # in dollar
    response = results['choices'][0]['message']['content'].strip()
    return response, cost

print(f'[INFO] Starting Gradio APP...')

with gr.Blocks() as app:
    gr.Markdown("### ChatGPT, please help to improve my paper writing!")

    # allow setting API key in gui
    api_input = gr.Textbox(label="OPENAI_API_KEY", value=openai.api_key, lines=1)

    # allow changing prompts
    init_prompt_input = gr.Textbox(label="Init Prompt", value=INIT_PROMPT)
    prefix_prompt_input = gr.Textbox(label="Prefix Prompt", value=PREFIX_PROMPT)

    temperature_input = gr.Number(value=1, label='temperature in [0, 2], the higher the more random.')
    simple_checkbox = gr.Checkbox(value=False, label='simple mode (only send the prefix prompt, cheaper)')

    with gr.Row():

        text_input = gr.Textbox(label="Input", lines=14)

        with gr.Column():
            text_output = gr.Textbox(label="Output", lines=10)
            cost = gr.Number(label='cost of this query ($)')

    text_button = gr.Button("Submit")
    text_button.click(submit, inputs=[text_input, api_input, init_prompt_input, prefix_prompt_input, temperature_input, simple_checkbox], outputs=[text_output, cost])
    
app.launch()