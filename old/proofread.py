'''
Proofread Module
MAxim Rebguns
V1.0.1
'''


def integer_check(inp, uptoanum, upmessage, downtoanum, downmessage, inv):
    import os
    go = False
    uptotrue = False
    downtotrue = False
    def upapprove():
        uptocheck = isinstance(uptoanum, int)
        if not uptocheck:
            print("ERR 2")
            print("The input for uptoanum is an invalid literal for int()")
            os._exit(0)
    def downapprove():
        downtocheck = isinstance(downtoanum, int)
        if not downtocheck:
            print("ERR 3")
            print("The input for downtoanum is an invalid literal for int()")
            os._exit(0)
    '''
    inpcheck = isinstance(inp, int)
    if not inpcheck:
        print("ERR 1")
        print("The input for inp is an invalid literal for int()")
        os._exit(0)
    '''
    if uptoanum == "x":
        uptotrue = True
    else:
        upapprove()
    if downtoanum == "x":
        downtotrue = True
    else:
        downapprove()
    approved = False
    while not approved:
        try:
            var = int(input(inp))
            go = False
            if uptotrue == False:
                #print("FALSE UPTOTRUE")
                if var > uptoanum:
                    print(upmessage)
                    go = True
            if downtotrue == False:
                #print("FALSE DOWNTOTRUE")
                if var < downtoanum:
                    print(downmessage)
                    go = True
            if go == False:
                #print("tru")
                approved = True
        except ValueError:
            print(inv)
    return var

def yes_or_no_check(ask, error_message):
    while True:
        query = input(ask)
        if "y" in query or "Y" in query:
            return True
        if "n" in query or "N" in query:
            return False
        else:
            print(error_message)
