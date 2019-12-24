class Tag:
    def __init__(self):
        self.tag_name = ""
        self.param_name = ""
        self.param_value = ""


class Equation:
    def __init__(self):
        self.var_name = ""
        self.var_value = 0


def evaluate_xml(xml_string):
    num_tags = 0
    slash_position = -1
    tag_list = []
    equations = []
    for i in range(len(xml_string)):
        if xml_string[i] == "<":
            tag_start_position = i
        elif xml_string[i] == "/":
            slash_position = i
        elif xml_string[i] == ">":
            tag_end_position = i
            if slash_position == -1:
                # vkladame novy tag na zasobnik
                new_tag = parse_tag(xml_string[(tag_start_position + 1):tag_end_position])
                tag_list.append(new_tag)
                process_tag(new_tag, equations)
            elif slash_position == (tag_end_position - 1):
                # neparovy tag, neukladame do zasobniku, ale musime parsovat kvuli vyhodnoceni vyrazu
                num_tags += 1
                new_tag = parse_tag(xml_string[(tag_start_position + 1):tag_end_position - 1])
                process_tag(new_tag, equations)
            elif slash_position == (tag_start_position + 1):
                # konec paroveho tagu
                slash_position = -1
                num_tags += 1
                # porovname pravou cast tagu s tim, co mame ulozene v zasobniku
                current_tag = tag_list.pop()
                if current_tag.tag_name != xml_string[(tag_start_position + 2):tag_end_position]:
                    print("text nevalidni")
                    exit()
    print("pocet tagu: ", num_tags, "\ntext validni ")
    for eq in equations:
        print(eq.var_name, "=", eq.var_value)

# rozdelime obsahu tagu s parametrem do objektu
def parse_tag(tag_string):
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


def process_tag(tag, equations):
    if tag.tag_name == "equation" and tag.param_name == 'variable':
        eq = Equation()
        eq.var_name = tag.param_value
        equations.append(eq)
    elif tag.tag_name == "add" and tag.param_name == "value":
        equations[-1].var_value += int(tag.param_value)
    elif tag.tag_name == "sub" and tag.param_name == "value":
        equations[-1].var_value -= int(tag.param_value)


# hlavni program:
xml_file = open("texthw04.xml", "r+")
file_content = xml_file.read()
evaluate_xml(file_content)
