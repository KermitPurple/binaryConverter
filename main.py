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

def main():
    for i in range(256):
        print(BinaryConverter.base10_to_binary(i))

if __name__ == "__main__":
    main()
