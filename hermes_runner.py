"""Run the official Hermes Agent with an OpenRouter-backed model.

This wrapper keeps secrets in the environment and delegates agent behavior to
Hermes instead of reimplementing Hermes inside this repository.
"""
import os
import shutil
import subprocess
import sys


def main() -> int:
    if not os.getenv("OPENROUTER_API_KEY"):
        print("OPENROUTER_API_KEY belum diset. Ikuti langkah di README.md.")
        return 1
    hermes = shutil.which("hermes")
    if not hermes:
        print("Perintah 'hermes' belum ditemukan. Install Hermes Agent terlebih dahulu.")
        return 1
    env = os.environ.copy()
    env.setdefault("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    env.setdefault("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    return subprocess.call([hermes, *sys.argv[1:]], env=env)


if __name__ == "__main__":
    raise SystemExit(main())
