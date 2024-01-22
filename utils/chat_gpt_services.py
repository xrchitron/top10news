from dotenv import load_dotenv
import os
import re
from openai import OpenAI
load_dotenv()  # Load environment variables from the .env file

def prompt_top_10_news_summary_stream(news):
    client = OpenAI(
        api_key=os.environ.get('CHATGPT_SECRET_KEY'),
    )
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[
               {"role": "system", "content": "You are a neutral news editor"},
               {"role": "user", "content": f"Select the top 10 significant news articles, remain the origin news url and provide a brief summary from the original news urls. Reference from the following news: {news}. And response news with format like this: [Title](url)\n   Summary\\n..."}
            ],
        stream=True,
    )
    message = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            message += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content or "", end="")
    return message


def process_prompt_top_10_news_message(message):
    news_items = re.split('\n\n', message)

    # Initialize an empty list to store the processed news items
    processed_news_items = []

    # Process each news item
    for news_item in news_items:
        # Step 2: Split the news item by newline character to separate the title, link, and description
        parts = re.split('\n', news_item)
        title_and_url = parts[0].split('(')
        title = title_and_url[0]
        url_part = title_and_url[1]
        url = url_part.strip(')')
        description = parts[1]

        # Step 3: Clean up each part
        cleaned_title = re.sub(r'\[|\]|1\. |2\. |3\. |4\. |5\. |6\. |7\. |8\. |9\. |10\. ', '', title).strip()
        # clean extra space
        cleaned_description = re.sub(r'\\n', '', description).strip()

        # Add the cleaned parts to the list of processed news items
        processed_news_items.append([cleaned_title, url, cleaned_description])
    return processed_news_items

# def prompt_top_10_news_summary():
#     request_url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#        "Content-Type": "application/json",
#        "Authorization": f"Bearer {os.environ.get('CHATGPT_SECRET_KEY')}"
#     }
#     news = news_from_newsapi()
#     data = {
#        "model": "gpt-4",
#        "messages": [
#           {"role": "system", "content": "You are a neutral news editor"},
#           {"role": "user", "content": f"Select the top 10 significant news articles,remain the origin news url and provide a brief summary from the original news urls. Reference from the following news: {news}"}
#        ],
#        "temperature": 0.7
#     }
#
#     response = requests.post(request_url, headers=headers, data=json.dumps(data))
#
#     json_content = response.json()
#     message = json_content['choices'][0]['message']['content']
#     return message