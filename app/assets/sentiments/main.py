import argparse
from scraper import parse

        
def classify(info):
    result = None
    return result


# def run(**params):
# 		URL = 'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q={query}&as_occt=any&as_drrb=b&as_mindate={month}%2F%{from_day}%2F{year}&as_maxdate={month}%2F{to_day}%2F{year}&tbs=cdr%3A1%2Ccd_min%3A3%2F1%2F13%2Ccd_max%3A3%2F2%2F13&as_nsrc=Gulf%20Times&authuser=0'
#     response = requests.get(URL.format(**params))
#     print response.content, response.status_code

def main():
    parser = argparse.ArgumentParser(description="Use frequencies to assign sentiment score.")
    parser.add_argument("filename", help="name of JSON file with links to financial articles")
    args = parser.parse_args()
    



    return 1
        
if __name__ == "__main__": main()
