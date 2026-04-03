from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Renders the home page with the text analysis form."""
    return render(request , 'index.html')
    
def Cases_to_utils_text(request):
    """
    Handles form submission for text formatting.
    Extracts text and applies the selected text analysis operations 
    such as removing punctuation, changing cases, and checking digit/alphabet compositions.
    Returns the results to the 'Cases_to_utils_text.html' template.
    """
    message = request.GET.get('text' , 'default')
    remove = request.GET.get('remove_punc' , 'off')
    uppercase = request.GET.get('upper_case' , 'off')
    lowercase = request.GET.get('lower_case' , 'off')
    title = request.GET.get('title' , 'off')
    caps = request.GET.get('capitalize' , 'off')
    isalnum_flag = request.GET.get('isallnum' , 'off')
    isalpha_flag = request.GET.get('isallpha' , 'off')

    analys_text1 = ""
    analys_text2 = ""
    analys_text3 = ""
    analys_text4 = ""
    analys_text5 = ""
    analys_text6 = ""
    analys_text7 = ""

# 1: Remove punctuations from the text
    if remove == 'on':
        punctuations = r'''!"$%&'()*+,-./:;<=>?@[\]^_`{|}~#'''    
        analys_text1 = ""

        for i in message:
            if i not in punctuations:
                analys_text1 = analys_text1 +  i
            message = analys_text1
    
# 2: Convert the entire text to uppercase
    if uppercase == 'on':
        analys_text2 = ''
        for char in message:
            analys_text2 = analys_text2 + char.upper()
        message = analys_text2

# 3: Check if all characters in the text are digits
    if isalnum_flag == 'on':
        cleaned_msg_num = message.replace(" ", "")
        analys_text3 = cleaned_msg_num.isdigit()
        message = analys_text3
        
# 4: Convert the entire text to lowercase
    if lowercase == 'on':
        analys_text4 = ''
        for char in  message:
            analys_text4 = analys_text4 + char.lower()
        message = analys_text4

# 5: Convert the text to title case
    if title == 'on':
        analys_text5 = message.title()
        message = analys_text5

# 6: Capitalize the first letter of the text
    if caps == 'on':
        analys_text6 = message.capitalize()
        message = analys_text6

# 7: Check if all characters in the text are alphabets
    if isalpha_flag == 'on':
        cleaned_msg_alpha = message.replace(" " , "")
        analys_text7 = cleaned_msg_alpha.isalpha()
        message = analys_text7

    # Check if no options were selected and return an error if true
    if remove != 'on' and uppercase != 'on' and lowercase != 'on' and title != 'on' and caps != 'on' and isalnum_flag != 'on' and isalpha_flag != 'on':
        error ={
            'error' : True
        }
        return render(request, 'index.html', error)

    # Prepare the context dictionary to pass to the template
    purpose = {
        "purpose1" : "Remove punctuations",
        "purpose2" : "UPPER CASE",
        "purpose3" : "Is all numbers",
        "purpose4" : "lower case",
        "purpose5" : "Title Case",
        "purpose6" : "Capitalize Case",
        "purpose7" : "Is all alphabet",

        "analyzed_text1" : analys_text1,
        "analyzed_text2" : analys_text2,
        "analyzed_text3" : analys_text3,
        "analyzed_text4" : analys_text4,
        "analyzed_text5" : analys_text5,
        "analyzed_text6" : analys_text6,
        "analyzed_text7" : analys_text7,

        "condition1" : remove,
        "condition2" : uppercase,
        "condition4" : lowercase,
        "condition3" : isalnum_flag,
        "condition5" : title,
        "condition6" : caps,
        "condition7" : isalpha_flag,

        "prev_text" : request.GET.get('text', 'default')
    }

    return render(request , 'Cases_to_utils_text.html' , purpose)
