import sys
from excalibur.excalibur import ExcaliburCore

def main():
    core = ExcaliburCore()
    print("Excalibur running. Enter 'exit' to quit.")
    while True:
        prompt = input("Query: ")
        if prompt.lower() == 'exit':
            break
        response = core.process_query(prompt)
        print("Response:", response)

if __name__ == "__main__":
    main()
