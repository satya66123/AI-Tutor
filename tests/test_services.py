from services.provider_service import ProviderService
from services.model_service import ModelService
from services.chat_service import ChatService

print("=" * 50)

print("Provider Available")

print(ProviderService.is_provider_available())

print("=" * 50)

print("Models")

models = ModelService.get_models()

for model in models:
    print(model)

print("=" * 50)

response = ChatService.generate_response(
    prompt="Introduce yourself in one sentence.",
    model=ModelService.get_default_model()
)

print(response)