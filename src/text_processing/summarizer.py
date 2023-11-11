import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model_name = "google/pegasus-xsum"
torch_device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = PegasusTokenizer.from_pretrained(model_name)

# Suppress initialization warning
with torch.no_grad():
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


def generate_math_summary(
    text, max_length=500, num_beams=5, length_penalty=2.0, no_repeat_ngram_size=2
):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="longest")
    translated = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=num_beams,
        length_penalty=length_penalty,
        no_repeat_ngram_size=no_repeat_ngram_size
    )
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text[0]


if __name__ == "__main__":
    from pathlib import Path

    base_path = Path.cwd()
    data_path = base_path / "data" / "summarize.txt"

    with open(data_path, "r") as f:
        text = f.read()

    summary = generate_math_summary(text)
    print(summary)
