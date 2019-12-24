class Tag:
    def __init__(self):
        self.tag_name = ""
        self.param_name = ""
        self.param_value = ""

def valid_test(xml_string):
    num_tags = 0
    slash_position = -1
    tag_list = []  # seznam tagu
    for i in range(len(xml_string)):
        if xml_string[i] == "<":
            tag_start_position = i
        elif xml_string[i] == "/":
            slash_position = i
        elif xml_string[i] == ">":
            tag_end_position = i
            if slash_position == -1:
                # append current tag name (start) on top of stack
                tag_list.append(xml_string[(tag_start_position + 1):tag_end_position])
            elif slash_position == (tag_end_position - 1):
                # neparovy tag
                num_tags += 1
            elif slash_position == (tag_start_position + 1):
                # konec paroveho tagu
                slash_position = -1
                num_tags += 1
                # porovname s tim, co mame ulozene v zasobniku (zacatek tagu)
                tag_name = tag_list.pop()
                if tag_name != xml_string[(tag_start_position + 2):tag_end_position]:
                    print("text nevalidni")
                    exit()
    print("pocet tagu: ", num_tags, "\ntext validni ")

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


download = open("texthw04.xml", "r+")
d = download.read()
valid_test(d)
