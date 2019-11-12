import os
from multiprocessing import cpu_count, Pool

from pylint import epylint as lint
from app.lib.pylint_errors import pylint_dict_final

is_linux = True

if os.name == "nt":
    is_linux = False

num_cores = cpu_count()


def process_error(error):
    """Formats error message into dictionary

        :param error: pylint error full text
        :return: dictionary of error as:
            {
                "code":...,
                "error": ...,
                "message": ...,
                "line": ...,
                "error_info": ...,
            }
    """
    # Return None if not an error or warning
    if error == " " or error is None:
        return None
    if error.find("Your code has been rated at") > -1:
        return None

    list_words = error.split()
    if len(list_words) < 3:
        return None

    # Detect OS
    line_num = None
    if is_linux:
        try:
            line_num = error.split(":")[1]
        except Exception as e:
            print(os.name + " not compatible: " + e)
    else:
        line_num = error.split(":")[2]

    # list_words.pop(0)
    error_yet, message_yet, first_time = False, False, True
    i, length = 0, len(list_words)
    # error_code=None
    while i < length:
        word = list_words[i]
        if (word == "error" or word == "warning") and first_time:
            error_yet = True
            first_time = False
            i += 1
            continue
        if error_yet:
            error_code = word[1:-1]
            error_string = list_words[i + 1][:-1]
            i = i + 3
            error_yet = False
            message_yet = True
            continue
        if message_yet:
            full_message = ' '.join(list_words[i:length - 1])
            break
        i += 1

    error_info = pylint_dict_final[error_code]

    return {
        "code": error_code,
        "error": error_string,
        "message": full_message,
        "line": line_num,
        "error_info": error_info,
    }


def format_errors(pylint_text):
    """Format errors into parsable nested dictionary

    :param pylint_text: original pylint output
    :return: dictionary of errors as:
        {
            {
                "code":...,
                "error": ...,
                "message": ...,
                "line": ...,
                "error_info": ...,
            }
            ...
        }
    """
    errors_list = pylint_text.splitlines(True)

    # If there is not an error, return nothing
    if "--------------------------------------------------------------------" in errors_list[1] and \
            "Your code has been rated at" in errors_list[2] and "module" not in errors_list[0]:
        return None

    errors_list.pop(0)

    pylint_dict = {}
    try:
        pool = Pool(num_cores)
        pylint_dict = pool.map(process_error, errors_list)
    finally:
        pool.close()
        pool.join()
        return pylint_dict

    # count = 0
    # for error in errors_list:
    #     pylint_dict[count]=process_error(error)
    #     count +=1
    # return pylint_dict


def evaluate_pylint(filename):
    """Create temp files for pylint parsing on user code

    :param text: user code
    :return: dictionary of pylint errors:
        {
            {
                "code":...,
                "error": ...,
                "message": ...,
                "line": ...,
                "error_info": ...,
            }
            ...
        }
    """
    # Open temp file for specific session.
    # IF it doesn't exist (aka the key doesn't exist), create one

    try:
        ARGS = " -r n --disable=R,C"
        (pylint_stdout, pylint_stderr) = lint.py_run(filename + ARGS, return_std=True)
    except Exception as e:
        raise Exception(e)

    if pylint_stderr.getvalue():
        raise Exception("Issue with pylint configuration")

    return format_errors(pylint_stdout.getvalue())


def check_code(filename):
    output = evaluate_pylint(filename)
    print(output)
    msg = ""
    if output is None:
        return msg
    for i in output:
        if i and isinstance(i, dict):
            msg += f"line {i.get('line')} : {i.get('message')}\n"
    return msg


strategy_template = """from ctpbee import CtpbeeApi
from ctpbee.constant import LogData, AccountData, PositionData


class StrategyClass(CtpbeeApi):
    def __init__(self, name, app=None):
        super().__init__(name, app)

    def on_trade(self, trade):
        pass

    def on_realtime(self):
        self.info("this is test message")

    def on_contract(self, contract):
        pass

    def on_order(self, order):
        pass

    def on_position(self, position: PositionData) -> None:
        pass

    def on_account(self, account: AccountData) -> None:
        pass

    def on_init(self, init):
        pass

    def on_tick(self, tick):
        \"""tick process function\"""

    def on_bar(self, bar):
        \"""bar process function\"""

ext = StrategyClass('strategy_name')


"""
