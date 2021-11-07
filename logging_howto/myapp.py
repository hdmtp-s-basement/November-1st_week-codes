import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO, format="%(levelname)s:%(message)s")
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == "__main__":
    main()