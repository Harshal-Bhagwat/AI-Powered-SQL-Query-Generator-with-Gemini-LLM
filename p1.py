import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyAZQy7PT9UZGvR14oVZRvB6Ted4qa7Z840")

# List all available models
for model in genai.list_models():
  # Only print models that support text generation
  if 'generateContent' in model.supported_generation_methods:
    print(model.name)