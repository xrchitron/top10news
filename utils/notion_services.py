def write_text(client, page_id, text, type):
    client.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": type,
                type: {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": text
                            }
                        }
                    ]
                }

            }
        ]
    )


def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']


def create_simple_blocks_form_content(client, content):
    page_simple_blocks = []

    for block in content:

        block_id = block['id']
        block_type = block['type']
        has_children = block['has_children']
        rich_text = block[block_type]["rich_text"]

        if not rich_text:
            return

        simple_block = {
            'id': block_id,
            'type': block_type,
            'text': rich_text[0]['plain_text']
        }

        if has_children:
            nested_children = read_text(client, block_id)
            simple_block['children'] = create_simple_blocks_form_content(client, nested_children)

        page_simple_blocks.append(simple_block)

    return page_simple_blocks


def safe_get(data, dot_chain_keys):
    keys = dot_chain_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except(KeyError, TypeError, IndexError):
            return None
    return data


def write_row(client, database_id, uuid, date_time, title, url, description):
    client.pages.create(
        **{
            "parent": {"database_id": database_id},
            "properties": {
                "Id": {
                    "title": [
                        {
                            "text": {
                                "content": uuid
                            }
                        }
                    ]
                },
                "Date": {
                    "date": {
                        "start": date_time
                    }
                },
                "Title": {
                    "rich_text": [
                        {
                            "text": {
                                "content": title,
                                "link": { "url": url }
                            }
                        }
                    ]
                },
                "Description": {
                    "rich_text": [
                        {
                            "text": {
                                "content": description
                            }
                        }
                    ]
                }
            }
        }
    )