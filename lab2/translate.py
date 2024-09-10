from googletrans import Translator
import sqlite3

translator = Translator()


def translate(str, lang):
    return translator.translate(str, dest=lang).text


def detect_lang(str):
    return translator.detect(str)


def code_lang(lang):
    con = sqlite3.connect("lab2/langs.db")
    cur = con.cursor()
    sql = "select code from langs where lang='%s'" % lang
    cur.execute(sql)
    lang = cur.fetchone()[0]
    con.close()
    return lang


print(translate("hello", "uk"))
print(detect_lang("hello world"))
print(code_lang("English"))
