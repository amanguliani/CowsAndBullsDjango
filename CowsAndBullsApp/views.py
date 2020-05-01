from django.shortcuts import render
from .forms import GuessWord
from .main_game import *
from operator import itemgetter

def index(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request, 'index.html')

def playgame(request):
    form = GuessWord(request.POST or None)
    secret_word = request.session.get('secret_word', "")

    if secret_word == "":
        request.session['secret_word'] = get_random_word(4)

    if 'GuessWord' in request.POST and form.is_valid():
        secret_word = request.session.get('secret_word').lower()
        guessed_word = form.cleaned_data['your_guess'].lower()
        clues_list = request.session.get('clues_list', [])
        request.session['error_in_guess'] = ''

        if is_win(secret_word, guessed_word):
            request.session['win'] = True
        elif len(clues_list) == 9:
            request.session['lose'] = True
        elif does_contain_repeated_words(guessed_word) \
                or is_not_valid_word(guessed_word)\
                or is_different_length(secret_word, guessed_word):
            request.session['error_in_guess'] = 'Invalid'
        elif guessed_word in list(map(itemgetter('Word'), clues_list)):
            request.session['error_in_guess'] = 'Duplicate'
        else:
            clues_list.append(calculate_bulls_and_cows(secret_word, guessed_word))
            request.session['clues_list'] = clues_list


    c = {
        'form': form,
        'secret_word': request.session.get('secret_word', ""),
        'game_in_progress': request.session.get("game_in_progress", False),
        'clues_list': request.session.get('clues_list', []),
        'error_in_guess': request.session.get('error_in_guess', ''),
        'win': request.session.get('win', False),
        'lose': request.session.get('lose', False),
    }
    return render(request, 'playgame.html', c)