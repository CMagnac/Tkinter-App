from random import shuffle
from .controller import MainApp
from .models import create_dictionary


def app():
    dct = create_dictionary()
    keyslist = list(dct.keys())
    shuffle(keyslist)
    app = MainApp(keyslist, dct)
    app.mainloop()
