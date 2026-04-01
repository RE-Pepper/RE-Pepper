#!/usr/bin/env python3
import questionary

maxlen = 0

def choose(items_dict, msg="Multiple matches found!"):
    global maxlen
    
    if not items_dict:
        return None

    # If only one, return that
    if len(items_dict) == 1:
        return next(iter(items_dict.values()))

    # for padding
    maxlen = max(len(str(k[0])) for k in items_dict.keys())

    choices = []
    for k, v in items_dict.items():
        left = k[0]
        # optional second option
        right = k[1] if len(k) > 1 and k[1] is not None else ""
        
        title = f"{left:<{maxlen}}    {right}".rstrip()
        choices.append(questionary.Choice(title=title, value=v))

    retval = questionary.select(
        message=msg+" Please select one: ",
        choices=choices
    ).ask()

    return retval
