
def FIND(txt, find_str):
    return txt.find(find_str)


def COMBINEVALUES(text1, text2, delimiter):
    return text1 + delimiter + text2


def CONCATENATE(lst, delimiter):
    return "'" + delimiter + "'".join(lst)


def LEN(text_str):
    return len(text_str)


def LOWER(text_str):
    return text_str.lower()


def UPPER(text_str):
    return text_str.upper()


def REPLACE(text, new_str, old_str):
    return text.replace(old_str, new_str)


def RIGHT(text, num_chars):
    length = len(text)
    return text[length - num_chars:]


def LEFT(text, num_chars):
    return text[:num_chars]


def SUBSTITUTE(text, old_str, new_str, instance_num):
    pass


def TRIM(text):
    return text.strip()


def UNICHAR(number):
    return chr(number)


def UNICODE(number):
    return chr(number)


def VALUE(text):
    return int(text)