import json

def get_ticker_types(file_path):
    file_path = 'data/tests/fetch_ticker_1.json'
    # file_path = 'data/stores/fetch_ticker.json'
    with open(file_path) as f:
        data = json.load(f)
    
    for k, v in data[0].items():
        print(k, type(v))
        if isinstance(v, dict):
            for k, v in v.items():
                print(k, type(v))
        elif isinstance(v, list):
            print(k, type(v))
            for i in v:
                print(type(i))

                    

if __name__ == '__main__':
    get_ticker_types()