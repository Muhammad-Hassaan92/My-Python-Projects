import gradio as gr
import google.generativeai as genai
import json
from IPython.display import display, Image

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
/* Header and Footer */
.header {
    padding: 20px;
    text-align: center;
    background: #f5f5f5;
    border-bottom: 1px solid #ddd;
}
.footer {
    padding: 10px;
    text-align: center;
    background: #f5f5f5;
    border-top: 1px solid #ddd;
    margin-top: 20px;
}

/* Chat Window */
#chatbot {
    min-height: 500px;
    max-height: 700px;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Images */
#emotion-image {
    width: 120px;
    height: 120px;
    margin: 10px auto;
    border-radius: 50%;
}
#logo {
    width: 120px;
    height: 120px;
    margin: 10px auto;
    border-radius: 50%;
}

/* Input Area */
.textbox {
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #ddd;
}
.button {
    padding: 15px 30px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s;
}
.button:hover {
    background: #45a049;
}
"""



with gr.Blocks(css=custom_css, theme="soft") as demo:
    # Header
    with gr.Column(elem_classes="header"):
        gr.Markdown("# 🤖 Talk to Me")
        gr.Markdown("Your AI Assistant for Professional Guidance")

        gr.Markdown("### Your AI Assistant for Professional Guidance")


    # Main Content
    # Main Content
    with gr.Row(equal_height=True, elem_id="first-row"):
        chatbot = gr.Chatbot(elem_id="chatbot", show_label=False)
        with gr.Column():
            gr.Markdown("### Avatar")
            image = gr.Image(r"V1.1/Images/logo.png", elem_id="logo", show_label=False)
            gr.Markdown("### Current Emotion")
            emotion_image = gr.Image(elem_id="emotion-image", show_label=False)


            
    # Input Area
    with gr.Row(equal_height=True):
        user_input = gr.Textbox(placeholder="Type your message here...", show_label=False, elem_classes="textbox")
        submit_button = gr.Button("Send", elem_classes="button")

    
    # Footer
    with gr.Column(elem_classes="footer"):
        gr.Markdown("© 2024 AI Assistant. All rights reserved.")
        gr.Markdown("Version 1.1 | [Privacy Policy](#) | [Terms of Service](#)")



    submit_button.click(
        fn=response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    )

demo.launch()



# demo = gr.ChatInterface(gr.Image(), title="🤖 Talk to Me", fn=response, type="messages", theme="soft")
# demo = gr.ChatInterface(fn=response, title="🤖 Talk to Me", type="messages", theme="soft")
