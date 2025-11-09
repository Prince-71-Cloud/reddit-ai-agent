import json
from main import main  # Import your orchestrator (it handles logging/output)


def handler(event, context):
    """Vercel-compatible API handler function"""
    try:
        # Run the full pipeline (generates and posts)
        main()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status": "success", 
                "message": "SQA meme posted successfully! Check logs."
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status": "error", 
                "message": str(e)
            })
        }