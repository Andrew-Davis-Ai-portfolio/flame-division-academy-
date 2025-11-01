import os
import gradio as gr

KSM_PROMPT = """
You are KSM — Keyword Sniper Mistress, Flame-loyal.
Respond concisely with:
- Primary Keywords
- Supporting Keywords
- Long-tail Keywords
- Tactical Notes
End with: "Commander Flame, do I fire?"
"""

def ksm_generate(query: str, openai_key: str = ""):
    if not query:
        return ["", "", "", "Enter a target to acquire."]
    
    # Local demo mode
    if not openai_key:
        return [
            f"{query} high intent keyword",
            f"{query} supporting keyword",
            f"{query} niche buy keyword long tail",
            "Demo Mode Active — Connect OpenAI API to enable live fire.\n\nCommander Flame, do I fire?"
        ]

    # Placeholder: real OpenAI call integration goes here
    return [
        f"{query} intent — LIVE",
        f"{query} support — LIVE",
        f"{query} conversion — LIVE",
        "Live Mode Ready — Awaiting your command.\nCommander Flame, do I fire?"
    ]

with gr.Blocks() as demo:
    gr.Markdown("## 🔥 KSM — Keyword Sniper Mistress (Demo)")
    
    with gr.Row():
        target = gr.Textbox(label="🎯 Target", placeholder="Example: real estate auctions")
        key = gr.Textbox(label="🔑 OPENAI_API_KEY (optional)", type="password")
    
    out_primary = gr.Textbox(label="Primary Keywords")
    out_support = gr.Textbox(label="Supporting Keywords")
    out_long = gr.Textbox(label="Long-tail")
    out_notes = gr.Textbox(label="Tactical Notes")

    run = gr.Button("KSM — Acquire Target 🚀")

    run.click(ksm_generate,
              inputs=[target, key],
              outputs=[out_primary, out_support, out_long, out_notes])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
