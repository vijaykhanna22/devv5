    assert add(-1, 1) == 0
>>>>>>> da5eafd21d1c940d075d2bb51d327324903b97e9
=======
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
=======
    assert add(-1, 1) == 0
>>>>>>> da5eafd21d1c940d075d2bb51d327324903b97e9
