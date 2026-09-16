# Binance Square Agent

This project generates English-language crypto articles and prepares them for publication on Binance Square while respecting a daily cap of 99 successful posts.

## Features
- Generates English crypto article content
- Prevents duplicate articles
- Performs a light review before publishing
- Tracks successful daily posts
- Supports GitHub Actions scheduling
- Stores records in SQLite and JSON logs

## Project structure
- `app/` - application logic
- `data/` - generated records and logs
- `.github/workflows/publish.yml` - scheduled execution on GitHub Actions
- `.env.example` - sample environment variables

## Local setup
1. Copy `.env.example` to `.env`.
2. Add your Binance Square API values.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python -m app.main
```

## GitHub Actions setup
Add the following repository secrets in GitHub:
- `BINANCE_SQUARE_API_KEY`
- `BINANCE_SQUARE_POST_URL`

## Important notes
- This project keeps the daily limit at 99 successful posts.
- The exact Binance Square API endpoint and payload structure must match the official documentation for your account/API configuration.
- Do not commit real secrets to the repository.

## License
MIT
