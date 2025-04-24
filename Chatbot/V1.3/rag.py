import gradio as gr
import numpy as np
from transformers import pipeline
# import whisper

# Load the ASR pipeline
speech_recognizer = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def transcribe(audio):
    # model = whisper.load_model("base")
    result = speech_recognizer(np.ndarray(np.array(audio)))
    print(result)
    return result["text"]

# Gradio UI
interface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(),  # Pass as NumPy array
    outputs="text",
    title="Speech to Text Transcription",
    description="Upload or record an audio file, and the model will transcribe it."
)

interface.launch()
