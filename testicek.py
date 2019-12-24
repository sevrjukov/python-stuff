class Tag:
    def __init__(self):
        self.tag_name = ""
        self.param_name = ""
        self.param_value = ""

def parseTag(tag_string):
    tag = Tag()
    if " " in tag_string:
        tag_parts = tag_string.split(" ")
        tag.tag_name = tag_parts[0]
        param_name_value = tag_parts[1].split("=")
        tag.param_name = param_name_value[0]
        tag.param_value = param_name_value[1][1:-1]
    else:
        tag.tag_name = tag_string
    return tag


tag = parseTag('a')

print(tag)
