# Bot 9Router + Hermes Agent

Project ini menggunakan **OpenRouter sebagai backend/model gateway** dan **Hermes Agent sebagai runtime AI agent**. Repository ini tidak menyalin source code Hermes; launcher memanggil instalasi Hermes resmi di komputer pengguna.

Arsitektur:

```text
Pengguna → Hermes Agent → OpenRouter API → Model AI
```

Hermes menyediakan agent loop, tools, memory, skills, dan interface. OpenRouter menyediakan akses ke model AI.

## Persyaratan

- Python 3.10 atau lebih baru
- Hermes Agent terpasang dan perintah `hermes` tersedia di PATH
- API key OpenRouter
- Koneksi internet

## Instalasi dan konfigurasi

```bash
git clone https://github.com/kevinsatrioc/bot_9router.git
cd bot_9router
```

Install Hermes Agent mengikuti dokumentasi resmi: https://hermes-agent.nousresearch.com/docs

```bash
hermes --help
```

Buat API key di https://openrouter.ai/keys, lalu set environment variable.

PowerShell:

```powershell
$env:OPENROUTER_API_KEY="isi_api_key"
$env:OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
$env:OPENROUTER_MODEL="openai/gpt-4o-mini"
```

Linux/macOS:

```bash
export OPENROUTER_API_KEY="isi_api_key"
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
export OPENROUTER_MODEL="openai/gpt-4o-mini"
```

## Menjalankan agent

```bash
python hermes_runner.py
python hermes_runner.py chat -q "Jelaskan tujuan project ini."
```

Semua argumen wrapper diteruskan ke Hermes. Jangan pernah commit API key; `.env` sudah dikecualikan oleh `.gitignore`.

## Struktur project

```text
hermes_runner.py   # launcher Hermes dengan backend OpenRouter
.env.example       # contoh konfigurasi tanpa secret
.gitignore         # mencegah secret ter-push
README.md          # panduan instalasi dan penggunaan
```

## Cara kerja

Pengguna mengirim pertanyaan ke Hermes Agent, Hermes menjalankan agent loop/tools, permintaan model dikirim ke OpenRouter, lalu respons diproses dan ditampilkan Hermes.

## Alur kontribusi grup

1. Buat branch: `git checkout -b fitur/nama-fitur`.
2. Kerjakan issue terkait dan uji lokal.
3. Commit, push branch, lalu buat Pull Request.
4. Minta review anggota lain sebelum merge.

## Keamanan

- Jangan mengunggah API key atau token.
- Jika key terlanjur terunggah, segera revoke dan buat key baru.
- Gunakan limit penggunaan OpenRouter.
- Jangan menjalankan tools Hermes dengan izin berlebihan di mesin produksi.
