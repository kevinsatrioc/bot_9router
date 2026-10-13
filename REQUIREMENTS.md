# Requirement Bot 9Router + Hermes Agent

Dokumen ini menjelaskan kebutuhan untuk menjalankan chatbot AI pada project ini.

## 1. Perangkat keras minimum

- Komputer atau server yang dapat menjalankan Python dan Hermes Agent
- RAM minimal 4 GB (8 GB disarankan jika menjalankan tools tambahan)
- Koneksi internet stabil
- Ruang penyimpanan minimal 1 GB untuk runtime dan dependency

> Model AI berjalan melalui OpenRouter, sehingga model tidak perlu diunduh ke komputer.

## 2. Software

- Python 3.10 atau lebih baru
- Git
- Hermes Agent resmi
- Terminal: PowerShell/CMD di Windows atau Bash di Linux/macOS

Periksa instalasi:

```bash
python --version
git --version
hermes --help
```

Instal Hermes Agent mengikuti dokumentasi resmi:

https://hermes-agent.nousresearch.com/docs

## 3. Akun dan kredensial

- Akun GitHub untuk mengambil source code
- Akun OpenRouter
- API key OpenRouter
- Model OpenRouter yang tersedia untuk akun tersebut

Buat API key di:

https://openrouter.ai/keys

Jangan masukkan API key ke source code, commit, issue, atau chat publik.

## 4. Environment variable wajib

```text
OPENROUTER_API_KEY=API key OpenRouter
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=openai/gpt-4o-mini
```

`OPENROUTER_BASE_URL` dan `OPENROUTER_MODEL` dapat diganti sesuai model yang dipilih. `OPENROUTER_API_KEY` wajib diisi.

## 5. File project

- `hermes_runner.py` — memeriksa konfigurasi lalu menjalankan Hermes Agent.
- `.env.example` — contoh nama environment variable tanpa secret.
- `.gitignore` — mencegah `.env`, cache, dan file lokal ikut di-push.
- `README.md` — panduan instalasi dan penggunaan.
- `REQUIREMENTS.md` — daftar kebutuhan project ini.

## 6. Alur instalasi

```bash
git clone https://github.com/kevinsatrioc/bot_9router.git
cd bot_9router
```

Setelah Hermes terpasang, konfigurasi environment.

PowerShell:

```powershell
$env:OPENROUTER_API_KEY="isi_api_key"
$env:OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
$env:OPENROUTER_MODEL="openai/gpt-4o-mini"
python hermes_runner.py
```

Linux/macOS:

```bash
export OPENROUTER_API_KEY="isi_api_key"
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
export OPENROUTER_MODEL="openai/gpt-4o-mini"
python hermes_runner.py
```

## 7. Kebutuhan saat development

- Branch terpisah untuk setiap fitur atau issue
- Pull Request untuk perubahan kode
- Review minimal satu anggota grup
- Pengujian lokal sebelum push
- Tidak ada secret di commit

## 8. Kebutuhan produksi

Sebelum deployment, siapkan:

- Secret manager atau environment variable yang aman
- Pembatasan biaya dan rate limit OpenRouter
- Logging tanpa membocorkan API key atau data sensitif
- Monitoring error dan penggunaan token
- Aturan akses tools Hermes yang paling terbatas
- Backup konfigurasi non-rahasia

## 9. Batasan

- Tanpa API key, chatbot tidak dapat meminta jawaban model melalui OpenRouter.
- Ketersediaan dan biaya model mengikuti OpenRouter.
- Hermes Agent harus sudah terpasang di setiap komputer anggota yang ingin menjalankan agent.
- Repository ini adalah konfigurasi dan launcher project, bukan salinan source code Hermes Agent.
