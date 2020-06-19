TRANSLATIONS = [
    "de",
    "en",
    "ru",
    "fr",
    "es",
    "it",
    "zh-TW"
]

TOKEN = "your_token_here"
ANDROID = "your_link_here"


def map_android(translation):
    if translation != ANDROID_BASE_LANGUAGE:
        return {
            ANDROID_FILE_KEY: "data/android/values-{}/strings.xml".format(translation),
            ANDROID_LANG_KEY: translation
        }

    else:
        return {
            ANDROID_FILE_KEY: "data/android/values/strings.xml",
            ANDROID_LANG_KEY: translation
        }


ANDROID_BASE_LANGUAGE = "en"
ANDROID_FILE_KEY = "file"
ANDROID_LANG_KEY = "lang"
ANDROID_FILES = map(map_android, TRANSLATIONS)
