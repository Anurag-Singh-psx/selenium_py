import random, string


class DataGenerator:
    @staticmethod
    def generate_random_string(length: int) -> str:
        characters = string.ascii_letters
        result_string = ''
        for i in range(length):
            result_string += random.choice(characters)
        return result_string

    @staticmethod
    def generate_random_number(length: int) -> str:
        number = string.digits
        result_number= ''
        for i in range(length):
            result_number += random.choice(number)
        return result_number
