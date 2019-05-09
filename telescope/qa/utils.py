import re


def extract_question_text(line):
    result = None
    try:
        result = re.match(".*\?", line).string
    except AttributeError:
        pass
        # This line is not a question
        return result
    else:
        # String leading hashes and spaces
        result = re.sub("^\s*#+\s+", "", result)
        return result
