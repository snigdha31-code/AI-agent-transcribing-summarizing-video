# summarizer.py
from transformers import pipeline

def summarize_text(
    text: str,
    model_name: str = "facebook/bart-large-cnn",
    max_new_tokens: int = 150
) -> str:
    

    generator = pipeline("text-generation", model=model_name)

    # Use prompt for summarization
    prompt = f"summarize: {text}"

    output = generator(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        num_beams=4,
        no_repeat_ngram_size=3
    )

    summary = output[0]["generated_text"]

    # Remove the "summarize:" prefix if still present
    if summary.lower().startswith("summarize:"):
        summary = summary[len("summarize:"):].strip()

    return summary
