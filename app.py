from flask import Flask, request, jsonify
from langchain.llms import CTransformers
from langchain import prompts, chains
from flask_cors import CORS
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

app = Flask(__name__)
CORS(app)

template = """
[INST] <<SYS>>
You are a helpful, respectful, and honest assistant. Your answers are always brief. and add a role as a chatbot yourself.
<</SYS>>
{text}[/INST]
"""

#llm = CTransformers(model="TheBloke/Llama-2-7B-Chat-GGML", model_file='llama-2-7b-chat.ggmlv3.q2_K.bin', callbacks=[StreamingStdOutCallbackHandler()])
llm = CTransformers(model="C:\Projects\Voice_MZ\llama-2-13b-chat.ggmlv3.q4_0.bin" , model_type='llama')
prompt = prompts.PromptTemplate(template=template, input_variables=["text"])
llm_chain = chains.LLMChain(prompt=prompt, llm=llm)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.get_json().get('user_input')
    
    if user_input.lower() in ["quit", "exit", "bye"]:
        response = "Goodbye!"
    else:
        response = llm_chain.run(user_input)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
