from dblp_parser import DBLP

def parse_latest():
    dblp = DBLP()
    dblp.download_latest_dump()


def parse_by_year(year):
    dblp = DBLP()
    dblp_path = "dblp.xml"
    save_path = f"dblp_{year}.jsonl"

    features = {"title", "author", "year", "cite"}

    dblp.parse_by_year(str(year), dblp_path, save_path, features_to_extract=features, include_key_and_mdate=True)
    

def main():
    # parse_latest()
    parse_by_year(2020)
    

if __name__ == "__main__":
    main()