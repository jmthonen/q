import os
import sys
from os import listdir, path
from typing import Any, Dict, List, Union
from glob import glob
from sbb_b import *

from sbb_b.helpers.functions.functions import translate

try:
    from yaml import safe_load
except ModuleNotFoundError:
    from sbb_b.helpers.functions.functions import safe_load
    

language = [os.environ.get("language") or "ar"]
languages = {}

for file in glob("strings/strings/*yml"):
    if file.endswith(".yml"):
        code = file.split("/")[-1].split("\\")[-1][:-4]
        try:
            languages[code] = safe_load(
                open(file, encoding="UTF-8"),
            )
        except Exception as er:
            LOGS.info(f"Error in {file[:-4]} language file")
            LOGS.exception(er)
            
            

def get_string(key: str, _res: bool = True) -> Any:
    lang = language[0]
    try:
        return languages[lang][key]
    except KeyError:
        try:
            ar_ = languages["ar"][key]
            tr = translate(ar_, lang_tgt=lang).replace("\ N", "\n")
            if ar_.count("{}") != tr.count("{}"):
                tr = en_
            if languages.get(lang):
                languages[lang][key] = tr
            else:
                languages.update({lang: {key: tr}})
            return tr
        except KeyError:
            if not _res:
                return
            return f"تحذير : لا يمكنك تحميل اي سلسلة مع المفتاح `{key}`"
        except TypeError:
            pass
        except Exception as er:
            LOGS.exception(er)
        if not _res:
            return None
        return languages["ar"].get(key) or f"فشل في تحميل سلسلة ترجمة ملف '{key}'"
      
      

def get_languages() -> Dict[str, Union[str, List[str]]]:
    return {
        code: {
            "name": languages[code]["name"],
            "natively": languages[code]["natively"],
            "authors": languages[code]["authors"],
        }
        for code in languages
    }
      
