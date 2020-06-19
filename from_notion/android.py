import json
from xml.dom import minidom
import os
from notion.client import NotionClient
from constants import TOKEN, ANDROID, ANDROID_LANG_KEY, ANDROID_FILE_KEY, ANDROID_FILES

client = NotionClient(token_v2=TOKEN)
database = client.get_collection_view(ANDROID)
current_rows = database.default_query().execute()

for translation in ANDROID_FILES:
    is_set = False
    language = translation[ANDROID_LANG_KEY]
    file = translation[ANDROID_FILE_KEY]

    doc = minidom.Document()
    root = doc.createElement('resources')
    doc.appendChild(root)

    for row in current_rows:
        key = row.get_property("key")
        value = row.get_property(language).replace("'", "\\'")

        if len(value) > 0:
            is_set = True
            string = doc.createElement('string')
            string.setAttribute("name", key)

            text = doc.createTextNode(value)
            string.appendChild(text)
            root.appendChild(string)

    if is_set:
        if not os.path.exists(os.path.dirname(file)):
            try:
                os.makedirs(os.path.dirname(file))

            except OSError as exc:
                print("Error")

        outfile = open(file, "w+")

        xml_as_string = root.toprettyxml()
        outfile.write(xml_as_string)

        outfile.close()
