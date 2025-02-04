import torch
from transformers import pipeline

# Load the Zephyr model (this may take time initially)
chatbot = pipeline(
    "text-generation", 
    model="HuggingFaceH4/zephyr-7b-alpha",
    torch_dtype=torch.bfloat16,  # Optimized for better performance
    device_map="cpu"  # Auto-detects available GPU/CPU
)

def generate_response(user_input):
    """Generates a response using Zephyr-7B."""
    
    # System message (you can change the chatbot's personality here)
    system_prompt = {
        "role": "system",
        "content": "You are a helpful AI assistant, friendly and informative.",
    }

    # Format messages as per Hugging Face's chat template
    messages = [
        system_prompt,
        {"role": "user", "content": user_input},
    ]
    
    # Convert messages to proper format
    formatted_prompt = chatbot.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # Generate response
    output = chatbot(formatted_prompt, max_new_tokens=10, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    
    # Extract and return generated response
    ai_reply = output[0]["generated_text"].split("<|assistant|>")[-1].strip()
    return ai_reply

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye!")
        break

    response = generate_response(user_input)
    print(f"AI: {response}")
