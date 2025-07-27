from googletrans import Translator
translator = Translator()


async def translate_text(to: str, text: str) -> str:
    try:
        async with Translator() as translator:
            translated = await translator.translate(text, dest=to)
            return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"


async def detect_languages(text: str):
    try:
        async with Translator() as translator:
            result = await translator.detect(text)
            return result.lang
    except Exception:
        return 'en'
        