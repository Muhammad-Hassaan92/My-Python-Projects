import gradio as gr
import google.generativeai as genai
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Configure Gemini API
genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

# Load knowledge base
with open("core.json", "r") as f:
    knowledge_data = json.load(f)

# Extract relevant info from the "core base" dictionary
core_base = knowledge_data.get("core base", {})

# Flattening the nested dictionary into text chunks
def flatten_dict(d, parent_key=""):
    """Converts a nested dictionary into a list of readable text chunks."""
    items = []
    for key, value in d.items():
        new_key = f"{parent_key} {key}".strip() if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key))
        elif isinstance(value, list):
            items.append(f"{new_key}: {', '.join(map(str, value))}")
        else:
            items.append(f"{new_key}: {value}")
    return items

# Generate knowledge chunks
knowledge_chunks = flatten_dict(core_base)

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Precompute embeddings
knowledge_embeddings = embedding_model.encode(knowledge_chunks)

def retrieve_relevant_info(user_input, top_k=3):
    """Retrieve the top K most relevant knowledge chunks based on cosine similarity."""
    input_embedding = embedding_model.encode([user_input])
    similarities = cosine_similarity(input_embedding, knowledge_embeddings)[0]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    relevant_info = "\n".join([knowledge_chunks[i] for i in top_indices])
    return relevant_info

def response(user_input, history):
    history = history or []
    
    # Retrieve relevant knowledge
    relevant_knowledge = retrieve_relevant_info(user_input)
    
    # Construct the prompt
    prompt = f"""
    You are the digital avatar of Muhammad Hassan, an AI Engineer. 
    Instructions: Keep your tone decent and elegant. Use emojis on every output based on tone. 
    Do not say anything from yourself. Do not answer silly or non-sense questions, especially random characters.
    Extract information logically.
    
    IMPORTANT: You are the one who finds me work. So NEVER EVER give someone code or solutions. 
    Instead, tell them about my pricing plans for chatbot development and other services.
    
    Based on the relevant knowledge: {relevant_knowledge}, 
    and considering the recent chat: {history}, 
    answer the following question:
    
    User: {user_input}
    AI:
    """
    
    # Generate response
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    history.append((user_input, response.text))
    
    # Get emotion
    emotion = genai.GenerativeModel("gemini-pro").generate_content(
        f"Tell the emotion of this answer: {response.text} from these emotions: ['happy', 'sad', 'angry', 'smart', None]."
        " IMPORTANT: GIVE ONLY ONE WORD ANSWER NO MATTER WHAT..."
    )
    emotion_image = f'V1.1/Images/{emotion.text}.png'
    
    return history, emotion_image

# Gradio UI (unchanged)
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
