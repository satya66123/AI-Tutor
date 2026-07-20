from providers.provider_manager import ProviderManager

print(ProviderManager.get_provider())

ProviderManager.set_provider("openai")

print(ProviderManager.get_provider())