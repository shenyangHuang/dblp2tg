from dblp_parser import DBLP

def parse_latest():
    dblp = DBLP()
    dblp.download_latest_dump()


def parse_by_year(year):
    dblp = DBLP()
    dblp_path = "dblp.xml"
    save_path = f"dblp_{year}.jsonl"
    dblp.parse_by_year(str(year), dblp_path, save_path)
    

def main():
    # parse_latest()
    parse_by_year(2024)
    

if __name__ == "__main__":
    main()