from argparse import ArgumentParser
from src.producer import producer
from src.consumer_input import consumer_input
from src.consumer_output import consumer_output

parser = ArgumentParser()
parser.add_argument("--action", dest="action", help="Your action: producer or consumer_input or consumer_output", default="consumer")

def main():
    args = parser.parse_args()
    action = args.action
    if action=="producer":
        producer()
    elif action=="consumer_input":
        consumer_input()
    elif action=="consumer_output":
        consumer_output()
    else:
      print("Invalid action. Please choose producer or consumer.")


if __name__ == '__main__':
    main()
