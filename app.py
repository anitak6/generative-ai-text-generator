from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

print("=== Generative AI Text Generator ===")

while True:
    prompt = input("\nEnter your prompt (or type 'exit'): ")
    
    if prompt.lower() == "exit":
        break

    result = generator(prompt, max_length=50, num_return_sequences=1)

    print("\nGenerated Text:")
    print(result[0]['generated_text'])
  
