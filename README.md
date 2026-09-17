# VanikBoost AI

VanikBoost AI is a full-stack project scaffold with a FastAPI backend and a React + Vite frontend.

## Project Structure

```text
backend/      Python + FastAPI app
frontend/     React + Vite app
database/     SQL/database setup
tests/        Automated tests
```

## Backend

```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

The API starts at `http://localhost:8000`.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend starts at `http://localhost:5173`.
