

def parse_t_f_message(answer):
    if answer == "" or answer == "\n" or answer == "Y":
        return True
    if answer == "n":
        return False
    raise Exception() 


t_f_text = "(Y/n) "

api_as_base = None
api_path = None
params = []
is_get = None
is_post = None
auto_log_msg = False
message_text = None

while api_as_base is None:
    try:
        api_as_base = parse_t_f_message(input("Do you want '/api' as base path? " + t_f_text))
    except Exception as e:
        print("Try again")

while api_path is None:
    try:
        api_path = input('Give me new route path\n')
        if api_path == "" or api_path == "\n":
            api_path = None
            break
        if api_path[0] != "/":
            api_path = "/" + api_path
        if api_path[-1] != "/":
            api_path = api_path + "/"
    except Exception as e:
        print("Try again")

add_param = True
while add_param is True:
    try:
        add_param = parse_t_f_message(input("Add param" + t_f_text))
        if not add_param:
            break
        new_param = None 
        while new_param is None:
            try:
                new_param = { "name": "", "type": ""}
                new_param["name"] = input("Param name:\n")
                if new_param["name"] == "" or new_param["name"] == "\n":
                    new_param = None
                    raise Exception() 
                new_param["type"] = input("Param type:\n")
                if new_param["type"] == "" or new_param["type"] == "\n":
                    new_param = None
                    raise Exception()
            except Exception as e:
                print("Try again") 

        params.append(new_param)
    except Exception as e:
        print("Try again")

while is_get is None:
    try:
        is_get = parse_t_f_message(input("Is it GET?" + t_f_text))
    except Exception as e:
        print("Try again")

while is_post is None:
    try:
        is_post = parse_t_f_message(input("Is it POST?" + t_f_text))
    except Exception as e:
        print("Try again")

add_log_message = None
while add_log_message is None:
    try:
        log_msg_sel = input("Log message (A-Auto/Y/n) ")
        if log_msg_sel == "A":
            auto_log_msg = True
            add_log_message = True
        elif parse_t_f_message(log_msg_sel):
            auto_log_msg = False
            add_log_message = True
        else:
            auto_log_msg = False
            add_log_message = False
    except Exception as e:
        print("Try again")

while message_text is None and add_log_message and not auto_log_msg:
    try:
        message_text = input("Give me message\n")
        if message_text == "" or message_text == "\n":
            message_text = None
    except Exception as e:
        print("Try again")

base_path = ""
if api_as_base:
    base_path = "/api"

params_str = ""
for p in params:
    params_str += "<{0}:{1}>/".format(p["type"], p["name"])

method_type = ""
if is_get:
    method_type += '"GET"'
    if is_post:
        method_type += ', '
if is_post:
    method_type += '"POST"'

decorator_str = '@app.route("{0}{1}{2}", methods=[{3}])'.format(base_path, api_path, params_str, method_type)

method_name = api_path.replace('/', "_").lower()[1:-1]
args_str = ""
for p in params:
    args_str += p["name"] + ", "
if args_str != "":
    args_str = args_str[:-2]

formater_log_str = ""
if add_log_message:
    if auto_log_msg:
        formater_log_str = "New request '{}'".format(api_path.replace('/', ' ')[1:-1])
        if len(params) > 0:
            formater_log_str = '"' + formater_log_str + " with params \\"
            for p in params:
                formater_log_str += f'\n\t\t\t{p["name"]}: ' + "{}, \\"
            formater_log_str = formater_log_str[:-3] + '".format('

            for p in params:
                formater_log_str += "{}, ".format(p["name"])
            formater_log_str = formater_log_str[:-2] + ')'
    else:
        formater_log_str = '"' + message_text + '"'

method_str = \
f'def {method_name}({args_str}):\n\
    @ExeptionHandler.abort_on_failure()\n\
    def {method_name}_impl({args_str}):\n\
        api_log({formater_log_str})\n\
        \n\
    return {method_name}_impl({args_str})\n'


print("\n Your api handler is done: \n\n" + decorator_str + "\n" + method_str)