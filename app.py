from const import *
from functions import * 
choice_nbr_days=input_choice('abc',menu_nbr_days)
choice_training=display_menu_by_days(choice_nbr_days)
display_exercices_of_choices(choice_nbr_days, choice_training)