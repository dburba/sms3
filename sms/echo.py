"""
Example sms message processor script to be used with subprocess server
"""
import sys


def main():
    """
    Accepts an incoming message, and sends back a message to the sender.
    """
    number = sys.stdin.readline()  # should begin with +1
    date = sys.stdin.readline()  # in iso format
    message = sys.stdin.readline()  # read message
    message = str(message, 'utf-8')  # convert utf-8 to unicode
    if number.startswith('+1'):
        # only respond if the sender has a valid number
        print(number[1:])  # respond with a number beginning with 1, not +1
        print('got')  # line breaks are OK
        print('yer')
        print('message')
        # respond with an ascii message. Optionally we could encode
        # message in a differnt format that the modem expects.
        print('"%s"' % message.encode('ascii', 'replace').strip())


if __name__ == '__main__':
    # run main function when called
    main()
