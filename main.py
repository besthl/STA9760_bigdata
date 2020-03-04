from sys import argv
from src.OPCV.getdata import Function
from os import environ

if __name__ == "__main__":
    app_key = environ.get("APP_KEY")
    #print page_size and num_pages
    page_size_str = argv[1]
    page_size = int(page_size_str.split('=')[1])
    num_pages_str = argv[2]
    num_pages = int(num_pages_str.split('=')[1])
    
    #print output
    try:
        output = argv[3]

    except Exception:
        output = None
    location = 'nc67-uf89'

    limit_size = int(page_size / num_pages)

    if output is None:
        with Function(app_key) as function:
            total_size = function.get_size(location)
            print(function.get_info(location, limit_size))
            offset = 0
            for i in range(num_pages-1):
                offset += limit_size
                if offset >= total_size:
                    break;
                print(function.get_next_info(location, limit_size, offset))
    else:
        output = output.split("=")[1]
        with Function(app_key) as function, open(output, "w") as fw:
            total_size = function.get_size(location)
            fw.write(f"{function.get_info(location, limit_size)}\n")
            offset = 0
            for i in range(num_pages-1):
                offset += limit_size
                if offset >= total_size:
                    break;
                fw.write(f"{function.get_next_info(location, limit_size, offset)}\n")
