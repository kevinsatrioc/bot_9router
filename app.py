"""Command-line entry point for Bot 9Router."""
from dotenv import load_dotenv

from src.chatbot import Chatbot, ConfigurationError, ChatbotError

load_dotenv()


def main() -> None:
    try:
        bot = Chatbot.from_environment()
    except ConfigurationError as exc:
        print(f"Konfigurasi belum lengkap: {exc}")
        return

    print("Bot 9Router siap. Ketik 'exit' atau 'quit' untuk keluar.")
    while True:
        try:
            message = input("Anda: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSampai jumpa!")
            break
        if message.lower() in {"exit", "quit", "keluar"}:
            print("Sampai jumpa!")
            break
        if not message:
            continue
        try:
            print(f"Bot: {bot.ask(message)}")
        except ChatbotError as exc:
            print(f"Bot gagal memproses pesan: {exc}")


if __name__ == "__main__":
    main()
