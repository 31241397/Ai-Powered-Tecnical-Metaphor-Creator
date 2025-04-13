# Technical Metaphor Creator - MetaForge

import gradio as gr
import os
import google.generativeai as genai  # Gemini API

# Configure Gemini API (replace with your actual key)
genai.configure(api_key="AIzaSyDOv5kDzDCLGoTKb57oCfKmatO715yar3g")
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_metaphor(concept, style):
    prompt = f"""
    You're a creative storyteller and technical educator.
    Explain the technical concept of '{concept}' using a {style} metaphor.
    Make it engaging, clear, and suitable for someone new to the topic.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="MetaForge: Technical Metaphor Generator") as app:
    gr.Markdown("""
    # 🧠 MetaForge
    *Craft creative metaphors to explain technical concepts with the help of AI.*
    """)

    with gr.Row():
        concept = gr.Textbox(label="🔍 Technical Concept", placeholder="e.g., Neural Network")
        style = gr.Dropdown(
            label="🎨 Metaphor Style",
            choices=["Simple Analogy", "Humorous", "Poetic", "Story-based"],
            value="Simple Analogy"
        )

    generate_btn = gr.Button("✨ Generate Metaphor")
    output = gr.Textbox(label="📝 Generated Metaphor", lines=6)

    generate_btn.click(fn=generate_metaphor, inputs=[concept, style], outputs=output)

app.launch()
