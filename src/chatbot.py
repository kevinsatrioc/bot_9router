"""Small OpenRouter client used by the command-line chatbot."""
import os
from dataclasses import dataclass, field
from typing import Dict, List

from openai import OpenAI


class ConfigurationError(Exception):
    """Raised when required environment configuration is missing."""


class ChatbotError(Exception):
    """Raised when the AI provider cannot answer."""


@dataclass
class Chatbot:
    client: OpenAI
    model: str = "openai/gpt-4o-mini"
    system_prompt: str = "Kamu adalah asisten yang ramah, jelas, dan membantu."
    messages: List[Dict[str, str]] = field(default_factory=list)

    @classmethod
    def from_environment(cls) -> "Chatbot":
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ConfigurationError("OPENROUTER_API_KEY belum diset. Salin .env.example menjadi .env.")
        return cls(
            client=OpenAI(
                api_key=api_key,
                base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
                default_headers={"HTTP-Referer": os.getenv("APP_URL", "http://localhost")},
            ),
            model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
        )

    def ask(self, message: str) -> str:
        if not message.strip():
            raise ValueError("Pesan tidak boleh kosong.")
        history = [{"role": "system", "content": self.system_prompt}, *self.messages]
        history.append({"role": "user", "content": message})
        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=history, temperature=0.7
            )
            answer = response.choices[0].message.content or "Maaf, bot tidak memberikan jawaban."
        except Exception as exc:
            raise ChatbotError(str(exc)) from exc
        self.messages.extend([
            {"role": "user", "content": message},
            {"role": "assistant", "content": answer},
        ])
        return answer
