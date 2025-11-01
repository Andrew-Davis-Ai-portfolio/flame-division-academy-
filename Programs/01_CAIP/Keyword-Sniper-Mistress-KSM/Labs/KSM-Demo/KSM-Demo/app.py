import random
import hashlib
import gradio as gr

COMMANDER = "Commander Flame"

KEYWORDS = {
    "Primary": [
        "AI Strategy", "Enterprise Automation", "Responsible AI",
        "AI Governance Framework", "LLM Integration"
    ],
    "Supporting": [
        "Model Risk Management", "AI Policy Templates",
        "Data Governance", "Change Management for AI",
        "Retrieval-Augmented Generation"
    ],
    "Long-Tail": [
        "how to deploy ai safely in a regulated industry",
        "ai governance checklist for midsize companies",
        "best llm integration pattern for crm",
        "ethical ai policy examples for finance",
        "raggenerator evaluation plan step by step"
    ],
}

def pseudo_metrics(term: str):
    """Deterministic fake metrics so the same term shows stable numbers."""
    h = int(hashlib.sha256(term.encode()).hexdigest(), 16)
    # Controlled ranges
    volume = 500 + (h % 9500)       # 500 – 9999
    difficulty = 15 + (h % 76)      # 15 – 90
    cpc_cents = 50 + (h % 950)      # $0.50 – $9.99
    cpc = round(cpc_cents / 100, 2)
    return volume, difficulty, cpc

def roll(mode: str, n: int):
    pool = KEYWORDS.get(mode, [])
    if not pool: return []
    picks = random.sample(pool, k=min(n, len(pool)))
    rows = []
    for t in picks:
        vol, diff, cpc = pseudo_metrics(t)
        why = (
            "High intent (conversion-ready)" if mode == "Primary" else
            "Mid-funnel pressure / authority build" if mode == "Supporting" else
            "Purchase-signal capture / sniper trap"
        )
        rows.append([t, vol, diff, f"${cpc}", why])
    return rows

def mission_brief(n_primary, n_support, n_long):
    primary = roll("Primary", n_primary)
    supporting = roll("Supporting", n_support)
    longtail = roll("Long-Tail", n_long)

    return primary, supporting, longtail, f"{COMMANDER}… authorization received. Targets locked."

with gr.Blocks(title="KSM — Keyword Sniper Mistress (Demo)") as demo:
    gr.Markdown("## 🔥 KSM — Keyword Sniper Mistress (Demo)")
    gr.Markdown("> “Commander Flame… do I fire?”")

    with gr.Row():
        n_primary = gr.Slider(1, 5, value=3, step=1, label="Primary (high-intent)")
        n_support = gr.Slider(1, 5, value=3, step=1, label="Supporting (mid-funnel)")
        n_long = gr.Slider(1, 5, value=3, step=1, label="Long-Tail (sniper traps)")

    fire = gr.Button("ACQUIRE ➜ CONFIRM ➜ FIRE")

    primary_out = gr.Dataframe(headers=["Primary Keywords","Volume","Difficulty","CPC","Why this wins for Flame"], datatype=["str","number","number","str","str"])
    support_out = gr.Dataframe(headers=["Supporting Keywords","Volume","Difficulty","CPC","Why this wins for Flame"], datatype=["str","number","number","str","str"])
    long_out = gr.Dataframe(headers=["Long-Tail Keywords","Volume","Difficulty","CPC","Why this wins for Flame"], datatype=["str","number","number","str","str"])
    status = gr.Markdown()

    fire.click(
        mission_brief,
        inputs=[n_primary, n_support, n_long],
        outputs=[primary_out, support_out, long_out, status]
    )

if __name__ == "__main__":
    demo.launch()
