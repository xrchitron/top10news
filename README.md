# Top 10 News [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

A workflow automation for **retrieving the top 10 important news, summarizing them, and storing them in the Notion database.**

## Process Chart

- Manage the execution schedule with Calendar.
- Activate the terminal to execute Python with Automator.
- Retrieve news data from NewsAPI and select 10 of them.
- Summarize the news and format them with a specific format.
- Stream the search results on the terminal.
- Store the results in Notion.

<div align="center">
<img width="90%" alt="Process Chart" src="https://github.com/xrchitron/top10news/blob/main/image/process_chart_diagram.jpg"/>
</div>

## Demo

- <video src=https://github.com/xrchitron/top10news/assets/125111607/0a971600-513a-4157-8fdb-e7d3a6e075a7>
     Sorry, your browser doesn't support embedded videos. ![Demo](https://youtu.be/4yHcKCIK61o)
  </video>

## How to Execute this Workflow Automation (The Following Method Is Only Doable with Apple Ecosystem)

1. Turn on the terminal and clone this file to your local device

   ```bash
   git clone https://github.com/xrchitron/top10news.git
   ```

2. Download the module in the project

   ```bash
   python3 -m pip install newsapi-python
   python3 -m pip install notion-client
   python3 -m pip install openai
   python3 -m pip install python-dotenv
   ```

3. Create a `.env` file which should reference the `.env.example` file. Populate it with the following keys:

   - `CHATGPT_SECRET_KEY`: Please reference [this link](https://elephas.app/blog/how-to-get-chatgpt-api-key-clh93ii2e1642073tpacu6w934j) for obtaining the ChatGPT API key.
   - `NEWS_SECRET_KEY`: Please reference [newsapi.org](https://newsapi.org/) for obtaining the News API key.
   - `NOTION_TOKEN`: Go to [Notion Developers](https://developers.notion.com/), click "view my integration," create a new integration, select the workspace, and provide a name for this integration.
   - `NOTION_PAGE_ID`: Go to your Notion page, click "Style, export and more...," "Add connections," and select the integration. Then click "Copy link" to get the page ID via the link: `https://www.notion.so/your_notion_domain/your_page_name-NOTION_PAGE_ID?pvs=4`.
   - `NOTION_DATABASE_ID`: Create a table with columns named Date, Title, Description, and id. Copy the link of the table, and you can get the database ID via the link: `https://www.notion.so/your_notion_domain/NOTION_DATABASE_ID?v=not_this_id&pvs=4`.

4. Turn on Automator and select "create application."

5. Search for "Run AppleScript" and paste the following code:

   ```applescript
   on run {input, parameters}
       tell application "Terminal"
           activate
           do script "python3 your/file/location/main.py"
       end tell
       return input
   end run
   ```

   - Replace `your/file/location/main.py` with the correct file address.

   - Save this application wherever you are comfortable managing it.

6. Create a schedule on the calendar and change the "alert" event to "Custom -> Open file." Choose the application file name and set the timing to activate.

7. Now you can schedule when to get the summarized news from ChatGPT. Remember to pay the balance when there is no quota in your ChatGPT account.

## Environment Setup

Python

## Authors

- **Yuhao Chen** - _Initial work_ - [xrchitron](https://github.com/xrchitron)

## License

This project is licensed under the MIT License
