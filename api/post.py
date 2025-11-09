import json
from main import main  # Import your orchestrator (it handles logging/output)
from fastapi import FastAPI  # pip install fastapi (optional, but recommended for Vercel)
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/post")  # Or POST for security
async def trigger_post():
    try:
        # Run the full pipeline (generates and posts)
        main()
        return JSONResponse({"status": "success", "message": "Post created! Check logs."})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

# For Vercel, the handler is auto-detected; no __init__.py needed
# Why this? Vercel runs functions on HTTP requests. Cron will "ping" this endpoint.
# If no FastAPI: Use plain def handler(request): and return dict (Vercel wraps it).
# Update main.py: Add print or return values for logs (Vercel captures stdout).