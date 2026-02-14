from typing import Tuple


class Solution:
    def __init__(self):
        self.word_dict = {
            1: "One ",
            2: "Two ",
            3: "Three ",
            4: "Four ",
            5: "Five ",
            6: "Six ",
            7: "Seven ",
            8: "Eight ",
            9: "Nine ",
            10: "Ten ",
            11: "Eleven ",
            12: "Twelve ",
            13: "Thirteen ",
            14: "Fourteen ",
            15: "Fifteen ",
            16: "Sixteen ",
            17: "Seventeen ",
            18: "Eighteen ",
            19: "Nineteen ",
            20: "Twenty ",
            30: "Thirty ",
            40: "Forty ",
            50: "Fifty ",
            60: "Sixty ",
            70: "Seventy ",
            80: "Eighty ",
            90: "Ninety ",
        }

    def numberToWords(self, number: int) -> str:
        if number == 0:
            return "Zero"

        result = ""

        while number > 0:
            magnitude = self.get_magnitude(number)
            chunk, number = self.get_chunk(number)

            result += self.prase_chunk(chunk) + magnitude

        return result.strip()

    def prase_chunk(self, chunk: int) -> str:
        result = ""
        hundreds = chunk // 100
        tens = chunk % 100
        ones = chunk % 10

        if hundreds:
            result += self.word_dict[hundreds] + "Hundred "

        if tens in self.word_dict.keys():
            result += self.word_dict[tens]
            return result

        if tens:
            result += self.word_dict[(tens // 10) * 10]
            result += self.word_dict[ones]

        return result

    def get_chunk(self, number: int) -> Tuple[int, int]:
        formatted = f"{number:,}".split(",")
        chunk, rest = int(formatted[0] or 0), int("".join(formatted[1:]) or 0)
        return chunk, rest

    def get_magnitude(self, number: int) -> str:
        magnitude = ["", "Thousand ", "Million ", "Billion "]
        length = len(str(number)) - 1

        return magnitude[length // 3]
