from dotenv import load_dotenv
import os
from notion_client import Client
from datetime import date
import uuid
import sys
sys.path.append('./utils')
from utils.notion_services import write_row
from utils.chat_gpt_services import prompt_top_10_news_summary_stream, process_prompt_top_10_news_message
from utils.news_services import news_from_news_api
from utils.json_services import json_to_dict
load_dotenv()  # Load environment variables from the .env file

notion_token = os.environ.get("NOTION_TOKEN")
notion_database_id = os.environ.get("NOTION_DATABASE_ID")
notion = Client(auth=notion_token)


def main():
    prompt_top_10_news = prompt_top_10_news_summary_stream(news_from_news_api())
    messages = process_prompt_top_10_news_message(prompt_top_10_news)
    for message in messages:
        write_row(notion, database_id=notion_database_id, uuid=str(uuid.uuid4()), date_time=str(date.today()), title=message[0], url=message[1],description=message[2])


if __name__ == "__main__":
    main()
