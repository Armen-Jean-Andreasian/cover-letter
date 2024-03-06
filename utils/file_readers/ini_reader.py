import configparser


def read_ini(ini_path: str, items: tuple[tuple[str, str], ...]) -> list[str]:
    """
    :param ini_path: path to ini file
    :param items: tuple((section_name, option_name), (section_name, option_name) )
    :return: list of str
    """
    config = configparser.ConfigParser()
    config.read(ini_path)
    results = []

    for item in items:
        section = item[0]
        option = item[1]

        result: str = config.get(section, option)
        results.append(result)

    return results
