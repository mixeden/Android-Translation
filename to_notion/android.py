import os
from xml.dom import minidom

from notion.client import NotionClient
from constants import TOKEN, ANDROID, ANDROID_FILES, ANDROID_FILE_KEY, ANDROID_LANG_KEY

client = NotionClient(token_v2=TOKEN)
database = client.get_collection_view(ANDROID)


def find_or_add_row(key):
    current_rows = database.default_query().execute()

    for row in current_rows:
        row_key = row.get_property("key")

        if row_key == key:
            return row

    row = database.collection.add_row()
    row.key = key

    return row


for translation in ANDROID_FILES:
    file_path = translation[ANDROID_FILE_KEY]
    print(file_path)

    if os.path.isfile(file_path):
        document = minidom.parse(file_path)
        elements = document.getElementsByTagName('string')

        for element in elements:
            key = element.attributes['name'].value
            value = element.firstChild.nodeValue
            language = translation[ANDROID_LANG_KEY]

            print("Getting key {} of {} language".format(key, language))

            new_row = find_or_add_row(key)
            new_row.set_property(language, value)
