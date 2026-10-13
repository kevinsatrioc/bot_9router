"""Run the official Hermes Agent with the local 9Router backend.

This wrapper keeps secrets in the environment and delegates agent behavior to
Hermes instead of reimplementing Hermes inside this repository.
"""
import os
import shutil
import subprocess
import sys


def main() -> int:
    if not os.getenv("NINEROUTER_API_KEY"):
        print("NINEROUTER_API_KEY belum diset. Ikuti langkah di README.md.")
        return 1
    hermes = shutil.which("hermes")
    if not hermes:
        print("Perintah 'hermes' belum ditemukan. Install Hermes Agent terlebih dahulu.")
        return 1
    env = os.environ.copy()
    env.setdefault("NINEROUTER_BASE_URL", "http://localhost:20128/v1")
    env.setdefault("NINEROUTER_MODEL", "default")
    # Hermes/provider adapters may use OpenAI-compatible variable names.
    env.setdefault("OPENAI_API_KEY", env["NINEROUTER_API_KEY"])
    env.setdefault("OPENAI_BASE_URL", env["NINEROUTER_BASE_URL"])
    env.setdefault("OPENAI_MODEL", env["NINEROUTER_MODEL"])
    return subprocess.call([hermes, *sys.argv[1:]], env=env)


if __name__ == "__main__":
    raise SystemExit(main())
