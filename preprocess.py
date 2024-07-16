import re
import sys
import json
import logging
import os

# Set up logging
logging.basicConfig(filename='preprocess_debug.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_func_doc(match):
    content = match.group(1)
    logging.debug(f"Matched content: {content}")
    params = {}
    for line in content.strip().split('\n'):
        key, value = line.split(':', 1)
        params[key.strip()] = value.strip()
    
    logging.debug(f"Parsed params: {params}")
    
    name_html = f'<span class="function-name">{params["name"]}</span>'
    args_html = f'<span class="function-args">({params["args"]})</span>' if 'args' in params else ''
    
    result = f'### <code>{name_html}{args_html}</code>\n\n{params["description"]}'
    logging.debug(f"Processed result: {result}")
    return result

def process_content(content):
    logging.debug("Processing content")
    pattern = r'\{\{func_doc\s+(.*?)\}\}'
    result = re.sub(pattern, process_func_doc, content, flags=re.DOTALL)
    logging.debug(f"Number of replacements: {content.count('{{func_doc') - result.count('{{func_doc')}")
    return result


if __name__ == "__main__":
    logging.debug("Script started")
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        logging.debug("Supports check")
        sys.exit(0)
    
    # Still process the book as before
    logging.debug("Reading from stdin")
    context, book = json.load(sys.stdin)
    
    for section in book['sections']:
        if 'Chapter' in section:
            logging.debug(f"Processing chapter: {section['Chapter'].get('name', 'Unnamed')}")
            section['Chapter']['content'] = process_content(section['Chapter']['content'])
            logging.debug(section['Chapter'])
            # loop through subsections
            for sub_item in section['Chapter'].get('sub_items'):
                if 'Chapter' in sub_item:
                    logging.debug(f"Processing subchapter: {sub_item['Chapter'].get('name', 'Unnamed')}")
                    sub_item['Chapter']['content'] = process_content(sub_item['Chapter']['content'])
                    logging.debug(sub_item['Chapter'])

        
    logging.debug("Writing to stdout")
    print(json.dumps(book))
    logging.debug("Script finished")