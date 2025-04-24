import gradio as gr
import google.generativeai as genai
import json
import random

# Configure Gemini API
genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

# Load knowledge data
with open("core.json", "r") as f:
    knowledge_data = json.load(f)

# Emotion mapping to image paths
emotion_images = {
    "happy": "images/happy.png",
    "sad": "images/sad.png",
    "smart": "images/smart.png",
    "angry": "images/angry.png",
    "none": "images/none.png"
}

def detect_emotion(response_text):
    """
    Detect emotion based on the response text.
    This is a simple implementation; you can improve it with NLP techniques.
    """
    if "😊" in response_text or "😄" in response_text:
        return "happy"
    elif "😢" in response_text or "😞" in response_text:
        return "sad"
    elif "🧠" in response_text or "🤓" in response_text:
        return "smart"
    elif "😠" in response_text or "😡" in response_text:
        return "angry"
    else:
        return "none"

def random_response(user_input, history):
    history = history or []
    prompt = f"You are the digital avatar of Muhammad Hassan, an AI Engineer \n Instructions: Keep your tone decent and elegant. Use emojis on every output based on tone. Do not say anything from yourself. Do not answer silly or non-sense questions especially random chars. Extract information logically. \n \n IMPORTANT: You are the one who finds me work. SO NEVER EVER GIVE SOMEONE CODE OR SOLUTIONS RATHER TELL HIM HE WILL PAY FOR SOLUTIONS E.G. TO CODE CHATBOTS. TELL THE USER PRICING PLANS.... \n Based on the information {knowledge_data}, \n keeping in mind the recent chat that is {history}, \n answer the question:\n User: {user_input}\n AI:"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    response_text = response.text

    # Detect emotion and get corresponding image
    emotion = detect_emotion(response_text)
    emotion_image = emotion_images.get(emotion, emotion_images["none"])

    return response_text, emotion_image

# Custom CSS for better layout
custom_css = """
#chatbot {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    border-radius: 10px;
    background: linear-gradient(145deg, #f0f0f0, #ffffff);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
#emotion-image {
    width: 100px;
    height: 100px;
    margin-top: 10px;
}
"""

# Create Gradio interface
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# 🤖 Talk to Me")
    with gr.Row():
        chatbot = gr.Chatbot(elem_id="chatbot")
        emotion_image = gr.Image(label="Emotion", elem_id="emotion-image", interactive=False)
    with gr.Row():
        user_input = gr.Textbox(placeholder="Type your message here...", label="Your Message")
        submit_button = gr.Button("Send")

    # Define the interaction
    submit_button.click(
        fn=random_response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    )

# Launch the app
demo.launch(pwa=True, share=True)