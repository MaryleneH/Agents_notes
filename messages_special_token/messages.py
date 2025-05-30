from transformers import AutoTokenizer

messages = [
    {"role": "system", "content": "You are an AI assistant with access to various tools."},
    {"role": "user", "content": "Hi !"},
    {"role": "assistant", "content": "Hi human, what can help you with ?"},
]

messages_in_french = [
    {"role": "system", "content": "Tu es un assistant IA avec des outils."},
    {"role": "user", "content": "Salut, toi !"},
    {"role": "assistant", "content": "Salut l'humain, comment puis-je t'aider ?"},
]

# Load the tokenizer and apply the chat template
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
rendered_prompt_in_french = tokenizer.apply_chat_template(messages_in_french, tokenize=False, add_generation_prompt=True)

print(rendered_prompt)
print(rendered_prompt_in_french)