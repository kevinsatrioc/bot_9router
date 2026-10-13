# Bot 9Router

Prototype chatbot berbasis Python yang menggunakan API [OpenRouter](https://openrouter.ai/) untuk mengakses model AI.

## Persyaratan

- Python 3.10 atau lebih baru
- API key OpenRouter
- Koneksi internet

## Instalasi

```bash
git clone https://github.com/kevinsatrioc/bot_9router.git
cd bot_9router
python -m venv .venv
```

Aktifkan virtual environment:

- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- Windows CMD: `.venv\\Scripts\\activate.bat`
- Linux/macOS: `source .venv/bin/activate`

Install dependency:

```bash
pip install -r requirements.txt
```

## Konfigurasi API key

1. Buat akun/login di OpenRouter dan buat API key di https://openrouter.ai/keys.
2. Salin `.env.example` menjadi `.env`.
3. Isi `OPENROUTER_API_KEY` dengan key milikmu.
4. Jangan pernah commit file `.env` ke GitHub.

Contoh Linux/macOS:

```bash
cp .env.example .env
```

Contoh Windows:

```powershell
Copy-Item .env.example .env
```

> Saat ini aplikasi membaca environment variable. Jalankan aplikasi dengan `OPENROUTER_API_KEY` tersedia di environment, atau tambahkan loader dotenv pada pengembangan berikutnya.

## Menjalankan chatbot

PowerShell:

```powershell
$env:OPENROUTER_API_KEY="isi_api_key"
python app.py
```

Linux/macOS:

```bash
export OPENROUTER_API_KEY="isi_api_key"
python app.py
```

Ketik pertanyaan pada prompt `Anda:`. Gunakan `exit`, `quit`, atau `keluar` untuk berhenti.

## Struktur project

```text
app.py              # entry point CLI
src/chatbot.py      # client OpenRouter dan riwayat percakapan
requirements.txt    # dependency Python
.env.example        # template konfigurasi
.gitignore          # file yang tidak boleh di-commit
```

## Alur kerja grup

1. Buat branch dari `main`: `git checkout -b fitur/nama-fitur`.
2. Kerjakan satu issue dalam satu branch.
3. Jalankan pengecekan lokal.
4. Commit dengan pesan yang jelas.
5. Push branch dan buat Pull Request.
6. Minta anggota lain melakukan review sebelum merge.

## Keamanan

- Jangan mengunggah API key ke repository.
- Jika key terlanjur terunggah, segera revoke dan buat key baru.
- Gunakan batas penggunaan OpenRouter untuk mencegah biaya tidak terduga.
