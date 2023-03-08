import time
class Pawel():
    @staticmethod
    def hello():
        time.sleep(5)
        print("hello from pawel ...")

def main():
    Pawel.hello()

if __name__ == "__main__":
    main()