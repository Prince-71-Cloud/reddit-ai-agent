import os
import json
from main import main  # Your orchestrator (generates/posts)
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()  # This 'app' is what Vercel looks for in ASGI mode

@app.get("/")  # Vercel maps /api/post to this function's root; use "/" to match
async def trigger_post():
    try:
        main()  # Runs your Reddit posting logic
        return JSONResponse({"status": "success", "message": "Post created! Check logs for URL."})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

# Optional: Add POST support for manual triggers with a secret key
@app.post("/")
async def trigger_post_secure():
    # Add auth if needed: if request.headers.get("Authorization") != "your-secret": return 401
    return await trigger_post()