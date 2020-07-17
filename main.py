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

class BinaryConverterTest(unittest.TestCase):

    def test_base10_to_binary(self):
        for i in range(10000):
            self.assertEqual(BinaryConverter.base10_to_binary(i), int(bin(i).replace("0b", "")))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
