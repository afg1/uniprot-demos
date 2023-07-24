from paperqa import Docs
import pickle
# get a list of paths
import os
import gradio as gr
from tqdm import tqdm

help_files = os.listdir("uniprot-manual/help")

if os.path.exists("uniprot_help.pkl"):
    with open("uniprot_help.pkl", "rb") as f:
        docs = pickle.load(f)
else:
    docs = Docs()
    for d in tqdm(help_files):
        try:
            docs.add(os.path.join("uniprot-manual/help", d ))#.replace("md", "txt")))
        except:
            print("error with", d)


with open("uniprot_help.pkl", "wb") as f:
    pickle.dump(docs, f)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        answer = docs.query(message)
        print(answer.formatted_answer)
        chat_history.append((message, answer.formatted_answer))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()



