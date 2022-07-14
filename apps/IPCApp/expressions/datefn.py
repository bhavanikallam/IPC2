import json
from apps.IPCApp.expressions.datefn import *

Exp = "exp"
Success = "success"
Error = "error"
Status = "status"
WorkType = "workType"


def substitute(exp, variables):
    try:
        for key, value in variables.items():
            exp = exp.replace(key, value)
        return exp
    except Exception as e:
        print(e.__str__())


def evaluate(params):
    response = {}
    try:
        expression = params.get(Exp)
        keys_to_exclude = {Exp, WorkType}
        variables = {k: v for k, v in params.items() if k not in keys_to_exclude}
        # printing the variables Json
        print("variables:- ", json.dumps(variables, indent=4))
        s = substitute(expression, variables)
        # printing the expression after substituting the variables
        print("expression:- ", s)
        eval_res = eval(s)
        response[Success] = True
        response[Status] = eval_res
    except Exception as e:
        response[Success] = False
        response[Error] = "failed to evaluate due to " + e.__str__()
        traceback.print_exc()
    return response


# if __name__ == "__main__":

    # input_params = {
    #     "exp": "DATEDIFF(__A__, __B__, __C__) + __D__",
    #     "__A__": "\"2020-03-21 12:30:00\"",
    #     "__B__": "\"2021-01-12 18:15:00\"",
    #     "__C__": "\"HOURS\"",
    #     "__D__": "1"
    # }

    # input_params = {
    #     "exp": "DATESBETWEEN(__A__, __B__, __C__)",
    #     "__A__": "\"2020-03-21\"",
    #     "__B__": "\"2021-01-12\"",
    #     "__C__": "\"months\""
    # }

    # res = evaluate(input_params)
    # print(res)
