import re
def add_linebreaks_even(string, length=50, recursive=False):
    """
    Will split the incoming text roughly even to match a given length. 
    Setting Recursive to true will allow the function to continue to filter
    through n passes when the sentance : length ratio of a given sentance
    inside the input string is greater than 1.

    n passes being any number of passes greater than 1 pass based off of the above
    ratio. 
    """
    find_n = re.finditer("(\n)", string)
    x_initial = 0
    composite_string = ''
    range_catcher = [0]

    
    for n in find_n:  # for every iteration find the distance between \n
        coords = n.span()
        x_final = coords[1]
        length_of_break_line = len(string[x_initial:x_final])
        break_string = string[x_initial:x_final]
        # print(break_string)
        # print(f"Length: {length_of_break_line}")
        # print(coords)

        len_range = length_of_break_line // length
        range_catcher.append(len_range)
    
        if length_of_break_line > length:
            iter_string = break_string  
            for _ in range(len_range + 1):
                index = length_of_break_line // 2
                while break_string[index] != " ":
                    if len_range % 2 != 0:
                        index += 1
                    else:
                        index -= 1
                if break_string[index] == " ":
                    iter_string = break_string[:index + 1] + "\n" + break_string[1 + index:]  # 
            composite_string += iter_string

        elif length_of_break_line < length:
            composite_string += break_string

        x_initial = x_final

    max_range =  max(range_catcher)
    count = max_range

    if  count > 0 and recursive == True:
        count -= 1
        return add_linebreaks_even(composite_string, recursive=True)
    
    return(composite_string)

def len_clean(raw_quote, doubles=False): # string
    """
    Adds line breaks at the end of every major punctuation (!, ?, .)
    The Double Feature will add double linebreaks. 
    """
    #print(len(raw_quote))  # debug
    options = ["!\n", "?\n", ".\n"]
    
    if doubles == True:
        for index, option in enumerate(options):
            option += "\n"
            options[index] = option

    exclaim, question, period = options
    sub_exclaim = re.sub(r"! ", exclaim, raw_quote) # break on !
    sub_question = re.sub(r"\? ", question, sub_exclaim)  # break on ?
    sub_period = re.sub(r"\. ", period, sub_question)  # break on .    
    sub_period +=  "\n"
    return sub_period


# test = "A lambda function is an anonymous function containing a single line expression. It can have any number of arguments, but only one expression can be evaluated. Here, the lambda function will append the string color for all the items present in the list and return the new value. Then using the list() function, we shall convert the map object returned by the map() function into a list."
# string = len_clean(test, doubles=True)
# print(string)

# even_r = add_linebreaks_even(string, recursive=True)
# even = add_linebreaks_even(string)

# print(even_r)
# print(even)

even_t = "Find a person who is as successful as you'd like to be, ask them what to do, do it and work hard."
break_t = len_clean(even_t, doubles=True)
print(add_linebreaks_even(break_t, recursive=True).strip())
