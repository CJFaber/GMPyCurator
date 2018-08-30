'''
GPMCQuestions.py

Contains all prompts used by the

'''


from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import os

# From PyInquirer list.py and input.py example



class DirValidator(Validator):
    def validate(self, document):
        ok = os.path.isdir(document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid directory',
                cursor_position=len(document.text))


class FileValidator(Validator):
    def validate(self, document):
        ok = os.path.isfile(document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid file',
                cursor_position=len(document.text))


def get_defaultdb():
    return os.getcwd() + 'db.json'


init_questions = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'Please Select a mode',
        'choices': [
            'Images',
            'Music',
            'Video'
        ]
    },
    {
        'type': 'input',
        'name': 'media_src',
        'message': 'Please specify a directory to scrape (Full path)\n',
        'validate': DirValidator
    },
    {
        'type': 'input',
        'name': 'media_dst',
        'message': 'Please specify a destination directory (Full path)\n',
        'validate': DirValidator
    },
    {
        'type': 'input',
        'name': 'database',
        'message': 'Please specify a (type tba) database\n',
        'default': lambda answers: os.getcwd() + '/db.csv',
        'validate': FileValidator
    }
]

init_style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',  # default
})