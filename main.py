import unittest

class BinaryConverter:

    @staticmethod
    def base10_to_binary(num: int) -> int:
        arr = []
        while True:
            arr.insert(0, num % 2)
            num //= 2
            if num <= 0:
                break
        return int("".join([str(i) for i in arr]))

    def binary_to_base10(num: int) -> int:
        s = str(num)
        output = 0
        for i in range(len(s)):
            output += int(s[i]) * 2 ** (len(s) - i - 1)
        return output

class BinaryConverterTest(unittest.TestCase):

    def test_base10_to_binary(self):
        for i in range(10000):
            self.assertEqual(BinaryConverter.base10_to_binary(i), int(bin(i).replace("0b", "")))

def main():
    # unittest.main()
    print(BinaryConverter.binary_to_base10(11111111))

if __name__ == "__main__":
    main()
