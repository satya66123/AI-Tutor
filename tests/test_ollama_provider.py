from providers.ollama_provider import OllamaProvider

provider = OllamaProvider()

print("=" * 50)
print("Ollama Available :", provider.is_available())

print("=" * 50)
print("Installed Models")

models = provider.list_models()

for model in models:
    print(model)

print("=" * 50)

response = provider.generate_response(
    prompt="Say Hello",
    model="qwen2.5:1.5b"
)

print(response)