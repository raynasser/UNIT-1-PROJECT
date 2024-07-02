

import numpy as np
from colorama import Fore, Style, Back, init




init(autoreset= True)

def color_genre(genre):
    colors = {
        'Animation': Back.MAGENTA,
        'Drama': Fore.GREEN,
        'Romantic': Back.LIGHTRED_EX,
        'Comedy': Fore.YELLOW,
        'Spy': Fore.LIGHTBLACK_EX,
        'Crime': Back.LIGHTBLACK_EX,
        'Thriller': Back.LIGHTWHITE_EX,
        'Adventure': Back.LIGHTMAGENTA_EX,
        'Documentary': Back.LIGHTGREEN_EX,
        'Horror': Back.RED,
        'Action': Back.LIGHTBLUE_EX,
        'Western': Back.CYAN,
        'Biography': Fore.BLUE,
        'Musical': Back.LIGHTYELLOW_EX,
        'Sci-Fi': Back.LIGHTCYAN_EX,
        'War': Back.LIGHTGREEN_EX,
        'Grotesque': Fore.LIGHTBLUE_EX,
        'Gangster': Back.YELLOW,
        'Fantasy': Back.RED,
        'Mélo': Fore.LIGHTCYAN_EX,
        'Mythology': Fore.LIGHTYELLOW_EX,
        'History': Back.GREEN,
        'Erotico': Fore.LIGHTRED_EX,
        'Noir': Back.BLACK,
        'Super-hero': Back.BLUE,
        'Biblical': Fore.MAGENTA,
        'Sport': Fore.LIGHTGREEN_EX,
        'Sperimental': Style.BRIGHT,
        np.nan: Fore.WHITE,  
        'Short Movie': Fore.LIGHTMAGENTA_EX,
        'Stand-up Comedy': Back.WHITE
    }

    return colors.get(genre, Fore.WHITE) + genre + Style.RESET_ALL
    