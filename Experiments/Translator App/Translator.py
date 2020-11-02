from timeit import timeit
from googletrans import Translator
from tkinter import *
from tkinter import ttk

# -- Configs ---

app_name = "@raddox7's First Translator App"
app_icon = "app_icon.ico"

# -- Supported Languages ---
LANG_KEYS = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn',
             'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka',
             'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga',
             'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg',
             'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro',
             'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg',
             'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

LANG_DICT = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
             'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
             'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
             'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican',
             'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
             'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french',
             'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek',
             'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew',
             'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic',
             'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
             'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
             'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
             'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy',
             'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
             'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
             'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese',
             'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic',
             'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala',
             'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese',
             'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu',
             'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
             'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}


# -- Functions ---

# Function: Starts benchmarking timer
def start_timer(prompt):
    global start
    start = timeit()
    print(prompt)


# Function: Stops and calculates timer
def stop_timer(prompt):
    if prompt is not None:
        print(prompt)
    global start, stop
    stop = timeit()
    print(f"Process finished in {stop - start}")


# Function: Returns True if auto_detect is On
def is_auto():
    return True if auto_detect.get() else False


# Function: Returns True if an [Enter] glitch occurs
def is_enter_glitch(text):
    return True if str(text.pronunciation)[-1] == "\n" else False


# Function: Set input language dropdown menu to match auto_detect language
def auto_update_language(source_text):
    lg_input.set(LANG_DICT[tr.detect(source_text).lang].title())


# Function: Returns pronunciation of a translated text
def get_pronunciation(text):
    return f"\n\nPronunciation: {text.pronunciation}"


# Returns a list of all languages in proper capitalization
def get_language_list():
    start_timer("Generating language list...")
    language_list = []
    for ID in LANG_KEYS:
        new_language = LANG_DICT.get(ID).title()
        language_list.append(new_language)
    stop_timer("Language generation process completed!")
    return language_list


# Function: Returns translated text
def get_translated_text(source_text, lang_input, lang_output):
    start_timer("Translating...")

    if is_auto():
        translated = tr.translate(source_text, lang_output, 'auto')
        auto_update_language(source_text)
    else:
        translated = tr.translate(source_text, lang_output, lang_input)

    if translated.pronunciation is None or is_enter_glitch(translated):
        stop_timer(f"Translation completed!\n{translated}")
        return translated.text
    else:
        stop_timer(f"Translation completed!\n{translated}")
        return translated.text + get_pronunciation(translated)


# -- Buttons ---

# Button: bt_translate
def button_translate():
    global bx_output
    bx_output.delete(0.0, END)
    bx_output.insert(0.0, get_translated_text(bx_input.get(0.0, END), lg_input.get(), lg_output.get()))


# -- Main ---

if __name__ == "__main__":

    # GUI Initialization
    gui = Tk()
    gui.title(app_name)
    # gui.iconbitmap(app_icon)

    # Translator Initialization
    tr = Translator(service_urls=["translate.google.com"])

    # Text: Powered by GoogleTranslate
    tx_powered = Label(text="Powered by Google Translate", bg="#4885ed", fg="white")
    tx_powered.grid(row=0, column=0, columnspan=4, sticky=W + E)

    # Input section
    tx_input = Label(text="From ")                                      # Text: "From"
    lg_input = StringVar()                                              # Input language variable
    dr_input = ttk.OptionMenu(gui, lg_input, *get_language_list())      # Input language dropdown menu
    lg_input.set(value='English')  # Input language default value
    bx_input = Text(gui, height=12, width=45)                           # Textbox: Input

    tx_input.grid(row=1, column=0, sticky=E)
    dr_input.grid(row=1, column=1, sticky=W)
    bx_input.grid(row=2, column=0, columnspan=2)

    # Output section
    tx_output = Label(text="To ")                                       # Text: "To"
    lg_output = StringVar()                                             # Output language variable
    dr_output = ttk.OptionMenu(gui, lg_output, *get_language_list())    # Output language dropdown menu
    lg_output.set(value='English')                                      # Output language default value
    bx_output = Text(gui, height=12, width=45)                          # Textbox: Output

    tx_output.grid(row=1, column=2, sticky=E)
    dr_output.grid(row=1, column=3, sticky=W)
    bx_output.grid(row=2, column=2, columnspan=2)

    # Checkbox: Automatically detect language?
    auto_detect = IntVar()
    auto_detect.set(value=1)
    ck_auto = ttk.Checkbutton(gui, text="Automatically detect source language", variable=auto_detect)
    ck_auto.grid(row=3, column=0, columnspan=2)

    # Button: Get translation
    bt_translate = ttk.Button(gui, text="Translate", command=button_translate)
    bt_translate.grid(row=3, column=2, columnspan=2)

    # End of the line
    gui.mainloop()
