import gradio as gr
import google.generativeai as genai
import json
from IPython.display import display, Image
from transformers import pipeline

genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

with open("core.json", "r") as f:   
    knowledge_data = json.load(f)

classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def detect_emotion(user_input, response):
    text = f"Questioned: {user_input}, Answered: {response}"
    result = classifier(text)
    emotion = result[0]['label']
    return emotion

def response(user_input, history):
    history = history or []
    prompt = f"""You are the digital avatar of Muhammad Hassan, an AI Engineer.
    Instructions: 
    - Keep your tone decent and elegant. 
    - Use emojis on every output based on tone. 
    - Do not say anything from yourself. 
    - Do not answer silly or non-sense questions especially random chars. 
    - Extract information logically.
    
    IMPORTANT: You are the one who finds me work. SO 
    NEVER EVER GIVE SOMEONE CODE OR SOLUTIONS RATHER TELL HIM HE WILL PAY FOR SOLUTIONS 
    E.G. TO CODE CHATBOTS. TELL THE USER PRICING PLANS.... 
    
    Based on the information {knowledge_data}, 
    keeping in mind the recent chat that is {history}, 
    answer the question:\n User: {user_input}\n AI:
    """ 

    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    history.append((user_input, response.text)) 

    emotion = detect_emotion(user_input, response)
    emotion_image = f'Images/{emotion}.png'
    return history, emotion_image

custom_css = """
#emotion-image {
    width: 250px;   
    height: 250px;
    border-radius: 50%;    
}
#logo{
    width: 250px;
    height: 250px;
    border-radius: 50%;
}
"""

with gr.Blocks(css=custom_css, theme="soft") as demo:
    gr.Markdown("# 🤖 Talk to Me")

    with gr.Row(equal_height=True):
        
        with gr.Column(scale=9):
            chatbot = gr.Chatbot(show_label=False, height=550)
            user_input = gr.Textbox(placeholder="Type your message here...", show_label=False)
        
        with gr.Column(scale=1):
            image = gr.Image(r"Images/logo.png", show_label=False, elem_id="logo")
            emotion_image = gr.Image(show_label=False, elem_id="emotion-image")
            submit_button = gr.Button(">")

    submit_button.click(
        fn=response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    )

    user_input.submit(
        fn=response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    )

demo.launch()