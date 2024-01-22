import json

def json_to_dict(content, file_name):
    # write_dict_to_file_as_json
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)