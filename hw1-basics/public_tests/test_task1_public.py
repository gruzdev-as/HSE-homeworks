from task1 import decode_caesar_cipher


def test_decode_basic_word():
    assert decode_caesar_cipher("Khoor, Zruog!", 3) == "Hello, World!"


def test_decode_shift_zero():
    assert decode_caesar_cipher("Same text.", 0) == "Same text."
