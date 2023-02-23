## ChatGPT, please help to improve my paper writing!

A thin wrapper of chatgpt with a gradio interface for improving academic writing.

The initialization prompt (also rewritten with chatgpt):
```
I would like to engage your services as an academic writing consultant to improve my writing. 
I will provide you with text that requires refinement, and you will enhance it with more academic language and sentence structures.
The essence of the text should remain unaltered, including any LaTeX commands. 
I request that you provide only the improved version of the text without any further explanations.
```

All of the following inputs are appended after the a prefix:
```
Please refine the following text in academic English: \n
```

![image](https://user-images.githubusercontent.com/25863658/220162062-21b0e6cc-acb4-457b-88af-5da7543593a2.png)

### Usage
```bash
### install
git clone https://github.com/ashawkey/chatgpt_please_improve_my_paper_writing.git
cd chatgpt_please_improve_my_paper_writing
pip install -r requirements.txt

### create a config.json and put your email/password/access_token into it.
# please refer to https://github.com/acheong08/ChatGPT for a valid config.
# usually the access_token from https://chat.openai.com/api/auth/session is enough.
cp config_example.json config.json

### run gradio
python main.py
```
