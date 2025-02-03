from transformers import pipeline

# Load the DialoGPT model using the pipeline
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye!")
        break

    # Generate response
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    ai_reply = response[0]['generated_text']
    
    print(f"AI: {ai_reply}")
