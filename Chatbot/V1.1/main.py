import gradio as gr
import google.generativeai as genai
import json
from IPython.display import display, Image

genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

with open("V1.0/core.json", "r") as f:   
    knowledge_data = json.load(f)

def show_img(emotion):
    display(Image(filename=f'V1.1/Images/{emotion}.png'))

def response(user_input, history):
    history = history or []
    prompt = f"You are the digital avatar of Muhammad Hassan, an AI Engineer \n Instructions: Keep your tone decent and elegant. Use emojis on every output based on tone. Do not say anything from yourself. Do not answer silly or non-sense questions especially random chars. Extract information logically. \n \n IMPORTANT: You are the one who finds me work. SO NEVER EVER GIVE SOMEONE CODE OR SOLUTIONS RATHER TELL HIM HE WILL PAY FOR SOLUTIONS E.G. TO CODE CHATBOTS. TELL THE USER PRICONG PLANS.... \n Based on the information {knowledge_data}, \n keeping in mind the recent chat that is {history}, \n answer the question:\n User: {user_input}\n AI:"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    emotion = genai.GenerativeModel("gemini-pro").generate_content(f"Tell the emotion of this Answer: {response} from these emotions: ['happy', 'sad', 'angry', 'smart', None] IMPORTANT: GIVE ONLY ONE WORD ANSWER NO MATTER WHAT...")
    gr.Image(type="filepath")
    # gr.Image(type="filepath", f"V1.1/Images/{emotion.text}.png")
    return response.text, emotion.text

# demo = gr.ChatInterface(gr.Image(type=f"V1.1/Images/{emotion}.png"), title="🤖 Talk to Me", fn=response, type="messages", theme="soft")
demo = gr.ChatInterface(fn=response, title="🤖 Talk to Me", type="messages", theme="soft")

demo.launch()