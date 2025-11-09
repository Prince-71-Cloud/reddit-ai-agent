import os
from ai_generator import generate_sqa_meme
from reddit_poster import RedditPoster
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main orchestrator function that generates SQA memes and posts to Reddit"""
    print("Starting SQA Meme Reddit AI agent...")
    
    # Generate SQA meme content using AI
    print("Generating SQA meme content...")
    content = generate_sqa_meme()
    
    print(f"Generated Title: {content['title']}")
    print(f"Generated Content Preview: {content['body'][:100]}...")
    
    # Post to Reddit
    print("Posting SQA meme to Reddit...")
    poster = RedditPoster()
    result = poster.post_to_reddit(
        title=content['title'],
        content=content['body']
    )
    
    if result['success']:
        print(f"Successfully posted SQA meme to Reddit! URL: {result['url']}")
        return result
    else:
        print(f"Failed to post SQA meme to Reddit: {result['error']}")
        return result

if __name__ == "__main__":
    main()