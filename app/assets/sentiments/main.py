import argparse
from scraper import parse


def main():
    parser = argparse.ArgumentParser(description="Use frequencies to assign sentiment score.")
    parser.add_argument("stock_sym", help="stock symbol of company")
    parser.add_argument("filename", help="name of JSON file with links to financial articles")
    args = parser.parse_args()
  	return parse(args.filename)

if __name__ == "__main__": main()
