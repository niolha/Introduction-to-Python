# 1.###################################################


def get_domains(filename):
    """
    The function returns names of Internet domains
    :param filename: str
    :return: list
    """
    with open(filename, 'r') as file:
        result = []
        for line in file.readlines():
            domain = line.strip()[1:]
            result.append(domain)
        return result


# def get_domains(filename):
#     try:
#         with open(filename, "r") as file:
#             return [line.strip()[1:] for line in file.readlines()]
#     except FileNotFoundError as error:
#         return f"THIS IS {error}"


print(get_domains("domains.txt"))


# 2.###################################################


# def get_surnames(filename):
#     """
#     The function returns surnames of Internet domains
#     :param filename:
#     :return: list
#     """
#     with open(filename, "r") as file:
#         return [line.split("\t")[1] for line in file.readlines()]


def get_surnames(filename):
    """
     The function returns surnames of Internet domains
     :param filename: str
     :return: list
     """
    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            surname = line.split('\t')[1]
            result.append(surname)
    return result


print(get_surnames('names.txt'))


# # 3.###################################################


def get_month_number(month_name):
    """
    The function modify month's names to numbers
    :param month_name: str
    :return: str
    """
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    return months[month_name]


def get_only_dates(filename):
    """
    The function returns list of dicts of original and modified dates
    :param filename: str
    :return: list of dicts
    """
    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            if "-" not in line:
                continue
            my_line = line.split(" - ")
            date = my_line[0]
            day, month, year = date.split()
            day = day[:-2]
            if len(day) < 2:
                day = f'0{day}'
            month = get_month_number(month)
            result.append({
                "date_original": date,
                "date_modified": f"{day}/{month}/{year}"
            })
    return result


print(get_only_dates("authors.txt"))
