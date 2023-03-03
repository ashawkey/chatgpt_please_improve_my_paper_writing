## ChatGPT, please help to improve my paper writing!

**NEW**: official API is also supported.

A thin wrapper of chatgpt with a gradio interface for improving academic writing.

The initialization prompt (also rewritten with chatgpt):
```
I would like to engage your services as an academic writing consultant to improve my writing. 
I will provide you with text that requires refinement, and you will enhance it with more academic language and sentence structures.
The essence of the text should remain unaltered, including any LaTeX commands. 
I request that you provide only the improved version of the text without any further explanations.
```

All of the later inputs are appended after this prefix:
```
Please refine the following text in academic English: \n
```



### Usage

#### Official
[api keys](https://platform.openai.com/account/api-keys)
```bash
### install
git clone https://github.com/ashawkey/chatgpt_please_improve_my_paper_writing.git
cd chatgpt_please_improve_my_paper_writing

pip install --upgrade gradio openai

### setup your API key 
export OPENAI_API_KEY=...
# or manually in official.py
openai.api_key = '...'

### run gradio
python official.py
```

#### Unofficial
[access token](https://chat.openai.com/api/auth/session)
```bash
### install
git clone https://github.com/ashawkey/chatgpt_please_improve_my_paper_writing.git
cd chatgpt_please_improve_my_paper_writing

pip install --upgrade --upgrade-strategy eager revChatGPT
pip install --upgrade gradio

### create a config.json and put your email/password/access_token into it.
# please refer to https://github.com/acheong08/ChatGPT for a valid config.
# usually the access_token from https://chat.openai.com/api/auth/session is enough.
cp config_example.json config.json

### run gradio
python unofficial.py
```

![image](https://user-images.githubusercontent.com/25863658/220972178-f9a343ac-04aa-4367-bd23-31402801b56b.png)

### Problems
* It is advisable to manually verify LaTeX math formulas, as the automatic process may occasionally miss important symbols such as underscores, slashes, or tildes. 
* In the event that the citation format appears incorrect, it is recommended to reset the chat and attempt the process again.
