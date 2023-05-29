from typing import Callable, Union


def get_fn_completions(name: Union[str, Callable]) -> Callable:
    """Get a decoder by name."""
    if not isinstance(name, str):
        return name

    if name == "anthropic_completions":
        from .anthropic import anthropic_completions

        return anthropic_completions
    elif name == "openai_completions":
        from .openai import openai_completions

        return openai_completions
    elif name == "huggingface_api_completions":
        from .huggingface_api import huggingface_api_completions

        return huggingface_api_completions

    elif name == "huggingface_local_completions":
        from .huggingface_local import huggingface_local_completions

        return huggingface_local_completions

    elif name == "cohere_completions":
        from .cohere import cohere_completions

        return cohere_completions

    else:
        raise ValueError(f"Unknown decoder: {name}")
