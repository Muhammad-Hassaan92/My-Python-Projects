import gradio as gr
import google.generativeai as genai
import json
from IPython.display import display, Image

# genai.configure(api_key="sk-046ea189addb4ae694eea932027d4739")
genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

with open("core.json", "r") as f:   
    knowledge_data = json.load(f)

def show_img(emotion):
    display(Image(filename=f'V1.1/Images/{emotion}.png'))

def response(user_input, history):
    history = history or []
    prompt = f"You are the digital avatar of Muhammad Hassan, an AI Engineer \n Instructions: Keep your tone decent and elegant. Use emojis on every output based on tone. Do not say anything from yourself. Do not answer silly or non-sense questions especially random chars. Extract information logically. \n \n IMPORTANT: You are the one who finds me work. SO NEVER EVER GIVE SOMEONE CODE OR SOLUTIONS RATHER TELL HIM HE WILL PAY FOR SOLUTIONS E.G. TO CODE CHATBOTS. TELL THE USER PRICONG PLANS.... \n Based on the information {knowledge_data}, \n keeping in mind the recent chat that is {history}, \n answer the question:\n User: {user_input}\n AI:"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    history.append((user_input, response.text)) 
    emotion = genai.GenerativeModel("gemini-pro").generate_content(f"Tell the emotion of this Answer: {response} from these emotions: ['happy', 'sad', 'angry', 'smart', None] IMPORTANT: GIVE ONLY ONE WORD ANSWER NO MATTER WHAT...")
    emotion_image = f'V1.1/Images/{emotion.text}.png'
    return history, emotion_image

custom_css = """
#emotion-image {
    width: 250px;   
    height: 100px;
    border: 1px solid blue;
    border-radius: 50%;    
}
#logo{
    width: 250px;
    height: 100px;
    border-radius: 50%;
    border: 1px solid blue;
}
"""

with gr.Blocks(css=custom_css, theme="soft") as demo:
    gr.Markdown("# 🤖 Talk to Me")

    with gr.Row(equal_height=True, elem_id="first-row"):
        chatbot = gr.Chatbot(elem_id="chatbot", show_label=False, scale=8, height=550)
        with gr.Column(scale=1):
            image = gr.Image(r"V1.1/Images/logo.png", elem_id="logo", show_label=False)
            emotion_image = gr.Image(elem_id="emotion-image", show_label=False)
            
    with gr.Row(equal_height=True):
        user_input = gr.Textbox(placeholder="Type your message here...", show_label=False, scale=9)
        submit_button = gr.Button(">", scale=1)

    submit_button.click(
        fn=response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    )

demo.launch()

# demo = gr.ChatInterface(gr.Image(), title="🤖 Talk to Me", fn=response, type="messages", theme="soft")
# demo = gr.ChatInterface(fn=response, title="🤖 Talk to Me", type="messages", theme="soft")
