from providers.model_manager import ModelManager

models = ModelManager.get_models()

print("=" * 40)
print("Available Models")
print("=" * 40)

for model in models:
    print(model)

print("=" * 40)
print("Default Model:")
print(ModelManager.get_default_model())