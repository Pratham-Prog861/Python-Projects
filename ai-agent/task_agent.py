import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv(dotenv_path=".env", override=True)

# Configure the API key
api_key = os.getenv('GEMENI_API_KEY')
if not api_key:
    raise ValueError("GEMENI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

def read_tasks(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    
def summarize_tasks(tasks):
    prompt = f"""
    You are smart task planning agent.
    Given a list of tasks, categorize them into three priority buckets:
    - High Priority
    - Medium Priority
    - Low Priority

    Tasks:
    {tasks}

    return the response in this format:
    High Priority:
    - Task 1
    - Task 2

    Medium Priority:
    - Task 1
    - Task 2

    Low Priority:
    ...
    """
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Generate the response
    response = model.generate_content(prompt)

    return response.text

if __name__ == "__main__":
    # Fixed typo in variable name (tast_text -> task_text)
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\n Task Summary: \n")
    print("-" * 30)
    print(summary)