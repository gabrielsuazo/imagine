from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


def initialisation():
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer


def calculate_word_probability(model, tokenizer, context, word):
    context_ids = tokenizer.encode(context, return_tensors='pt')
    word_id = tokenizer.encode(word, add_special_tokens=False)[0]

    with torch.no_grad():
        outputs = model(context_ids)
        logits = outputs.logits[0, -1, :]

    probs = torch.nn.functional.softmax(logits, dim=-1)
    word_prob = probs[word_id].item()
    max_prob = torch.max(probs).item()
    relative_prob = word_prob / max_prob
    return relative_prob


context = "Once upon a midnight"
word = " dreary"
model, tokenizer = initialisation()
probability = calculate_word_probability(model, tokenizer, context, word)
print(f"Probability of '{word}' given context '{context}': {probability}")
