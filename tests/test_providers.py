from providers.provider_manager import ProviderManager
from providers.provider_factory import ProviderFactory


providers = [
    "ollama",
    "openai",
    "anthropic"
]

for provider_name in providers:

    print("=" * 50)

    print(provider_name.upper())

    ProviderManager.set_provider(provider_name)

    provider = ProviderFactory.get_provider()

    print("Available :", provider.is_available())

    print("Models :")

    models = provider.list_models()

    print(models)

    if provider.is_available() and models:

        response = provider.generate_response(
            "Say hello in one sentence.",
            models[0]
        )

        print(response)