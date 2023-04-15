from datetime import datetime


def get_date_from_string(date_str, format_):

    return datetime.strptime(date_str, format_)


if __name__ == "__main__":
    date_ = "2022.02.21"
    format_ = "%Y.%m.%d"
    print(f"main is running and the date is {get_date_from_string(date_, format_)}...")
