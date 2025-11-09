import os
import openai
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sqa_meme():
    """
    Generate SQA (Software Quality Assurance) meme content for Reddit
    """
    try:
        # Different types of SQA memes to alternate
        meme_types = [
            "silly_situation",
            "relatable_bug_hunt",
            "tester_vs_dev",
            "automated_testing",
            "manual_testing",
            "regression_testing",
            "frustration_moment",
            "victory_bug_fix",
            "user_reported_issue"
        ]
        
        selected_type = random.choice(meme_types)
        
        # Different prompts based on meme type for variety
        prompts = {
            "silly_situation": "Generate a humorous Software Quality Assurance meme idea about a tester in a completely absurd testing situation. Include a funny title and a detailed description that could be turned into an image meme.",
            "relatable_bug_hunt": "Generate a Software Quality Assurance meme about a relatable bug hunting experience that testers often encounter. Include a catchy title and a description that captures the shared experience of SQA professionals.",
            "tester_vs_dev": "Generate a funny Software Quality Assurance meme highlighting the classic tester vs developer relationship dynamic. Include a title and description that shows the humorous side of their collaboration.",
            "automated_testing": "Generate a Software Quality Assurance meme about the joys and challenges of automated testing. Include a title and description focusing on the realities of automated testing processes.",
            "manual_testing": "Generate a Software Quality Assurance meme about the dedication required for manual testing. Include a title and description that highlights the human touch in testing.",
            "regression_testing": "Generate a Software Quality Assurance meme about regression testing - the never-ending cycle. Include a title and description that captures the essence of regression testing.",
            "frustration_moment": "Generate a Software Quality Assurance meme about a tester's frustrating moment when a bug reappears after being marked as fixed. Include a title and description showing the relatable frustration.",
            "victory_bug_fix": "Generate a Software Quality Assurance meme celebrating a tester's victory when finding a critical bug before release. Include a title and description that shows the tester's triumph.",
            "user_reported_issue": "Generate a Software Quality Assurance meme about receiving an unclear bug report from a user. Include a title and description about the challenge of reproducing user-reported issues."
        }
        
        prompt = prompts[selected_type]
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert meme creator for Software Quality Assurance professionals. Create funny, relatable and engaging SQA memes that resonate with testers, QA engineers, and developers. The content should be appropriate for Reddit and include situations that SQA professionals commonly experience. Include both a title that would work for a Reddit post and a body that describes the meme setup."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.8  # Higher temperature for more creative/variety
        )
        
        content = response.choices[0].message.content.strip()
        
        # Extract title and body from the response
        lines = content.split('\n')
        title = lines[0].strip('# "') if lines else "SQA Meme: Another Day in Testing"
        # Remove prefixes like "Title:" or "Meme:" if present
        if title.lower().startswith("title:"):
            title = title[6:].strip()
        elif title.lower().startswith("meme:"):
            title = title[5:].strip()
        
        body = '\n'.join(lines[1:]).strip() if len(lines) > 1 else content
        
        # Ensure the title is appropriate length for Reddit
        if len(title) > 300:
            title = title[:297] + "..."
        
        return {
            "title": title,
            "body": body
        }
    except Exception as e:
        print(f"Error generating SQA meme: {e}")
        # Fallback SQA memes to return if API fails
        fallback_memes = [
            {
                "title": "When the dev says 'It works on my machine' for the 100th time",
                "body": "SQA Reality: It works on my machine ≠ It works in production.\n\nA classic developer excuse that every tester has heard countless times. The difference between local environment and production can be huge!"
            },
            {
                "title": "Me: 'Found a bug!' Dev: *fixes it* Me: 'Found another bug!'",
                "body": "The endless cycle of bug hunting. Just when you think you're done testing, you find another issue. It's not a bug, it's a feature that was added by mistake!"
            },
            {
                "title": "When you finally reproduce that intermittent bug after 2 hours",
                "body": "Tester's victory dance: Finally got the steps to reproduce! Now I just need to document it before it disappears again."
            }
        ]
        return random.choice(fallback_memes)

if __name__ == "__main__":
    # Test the function
    result = generate_sqa_meme()
    print("Generated Title:", result["title"])
    print("Generated Body:", result["body"])