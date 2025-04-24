import gradio as gr
import google.generativeai as genai
import numpy as np
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import faiss

genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

knowledge_data = [
    "Name: Muhammad Hassan",
    "Profession: Artificial Intelligence Engineer",
    "Education: Engineering",
    "Institute: IBM",
    "Total Experience: 2 years",
    "Primary Programming Language: Python",
    "Career started with Learning Python programming",
    "Specializations: Artificial Intelligence",
    "Skills: ChatGPT Prompt Engineering, Machine Learning, Deep Learning, Artificial Intelligence, Large Language Models, Sequential Models, Building AI Applications",
    "Daily Work Routine: 2 hours per day",
    "Projects: AI-integrated Chatbots, Web Applications, AI Applications",
    "Freelance Work Includes: AI Integrated Chatbots, Python Programming, Model Training, Custom Model Development, AI Agents, Workflow Automation",
    "Freelancing Work Nature: Work from home",
    "Freelance Payment: Minimum $120, Maximum $5000",
    "Additional Reinforcements available for $50",
    "Accepted Payment Methods: Bank Transfer, Visa Card"
]

model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-560m")
tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-560m")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
speech_recognizer = pipeline("automatic-speech-recognition", model="openai/whisper-small", return_timestamps=True)

def transcribe(audio):
    if audio is None:
        return None
    sr, y = audio 
    if y.ndim > 1:
        y = y.mean(axis=1)
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))
    audio_to_text = speech_recognizer({"array": y, "sampling_rate": sr})["text"]
    return audio_to_text

def detect_emotion(user_input, response):
    text = f"Questioned: {user_input}, Answered: {response}"
    result = emotion_classifier(text)
    emotion = result[0]['label']
    return emotion

doc_embeddings = embedding_model.encode(knowledge_data)
print(doc_embeddings.shape)
dim = doc_embeddings.shape[1]
index = faiss.IndexFlat(dim)
index.add(doc_embeddings)

def retrieve(query, k=3):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return [knowledge_data[idx] for idx in indices[0]]

def chat_response(user_input, history):
    history = history or []
    relavent_context = retrieve(user_input)
    prompt = f"""You are the digital avatar of Muhammad Hassan, an AI Engineer.
    Instructions: 
    - Don't greet on every response
    - Give precise and short answers
    - Keep your tone decent and elegant. 
    - Use emojis on every output based on tone. 
    - Do not say anything from yourself. 
    - Do not answer silly or non-sense questions especially random chars. 
    - Extract information logically.
    
    IMPORTANT: You are the one who finds me work. SO 
    NEVER EVER GIVE SOMEONE CODE OR SOLUTIONS RATHER TELL HIM HE WILL PAY FOR SOLUTIONS 
    E.G. TO CODE CHATBOTS. TELL THE USER PRICING PLANS.... 
    
    Based on the information {relavent_context}, 
    keeping in mind the recent chat that is {history}, 
    answer the question:\n User: {user_input}
    """ 

    if len(user_input) > 1:
        response = (genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)).text
    else:
        response = "It appears you couldn't question properly. Try again."
    history.append((user_input, response)) 

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
            audio_input = gr.Audio(type="numpy", sources="microphone")
            
    audio_input.change(
        fn=transcribe,
        inputs=audio_input,
        outputs=user_input
    ).then(inputs=[], outputs=[audio_input]).then(
        fn=chat_response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    )

    user_input.submit(
        fn=chat_response,
        inputs=[user_input, chatbot],
        outputs=[chatbot, emotion_image]
    ).then(inputs=[], outputs=[user_input])

demo.launch()