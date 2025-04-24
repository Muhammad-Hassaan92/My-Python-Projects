import gradio as gr
import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

with open("core.json", "r") as f:   
    knowledge_data = json.load(f)

def random_response(user_input, history):
    history = history or []
    prompt = f"You are the digital avatar of Muhammad Hassan, an AI Engineer \n Instructions: Keep your tone decent and elegant. Use emojis on every output based on tone. Do not say anything from yourself. Do not answer silly or non-sense questions especially random chars. Extract information logically. \n \n IMPORTANT: You are the one who finds me work. SO NEVER EVER GIVE SOMEONE CODE OR SOLUTIONS RATHER TELL HIM HE WILL PAY FOR SOLUTIONS E.G. TO CODE CHATBOTS. TELL THE USER PRICONG PLANS.... \n Based on the information {knowledge_data}, \n keeping in mind the recent chat that is {history}, \n answer the question:\n User: {user_input}\n AI:"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt) 
    return response.text

demo = gr.ChatInterface(title="🤖 Talk to Me", fn=random_response, type="messages", multimodal=True, theme="soft")

demo.launch()