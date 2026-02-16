
# SimpleAI Voice Processor Backend

## Setup

1.  **Create Virtual Environment**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

Start the FastAPI server with hot-reloading:

```bash
uvicorn app.main:app --reload
```

Server will be running at: `http://127.0.0.1:8000`
Docs available at: `http://127.0.0.1:8000/docs`

## Testing

A simulation script is provided to test the full pipeline (Webhook -> Analysis -> Background Task -> DB/PDF).

1.  Ensure the server is running in one terminal.
2.  Run the simulation script in another terminal:

```bash
python test_simulation.py
```

## Internal Architecture

- **`app/main.py`**: Entry point.
- **`app/api/endpoints.py`**: Receives the webhook.
- **`app/services/call_processor.py`**: Main orchestration logic.
- **`app/workers/background_tasks.py`**: Handles inventory updates and PDF generation asynchronously.
- **`generated_invoices/`**: Folder where PDFs will appear.
