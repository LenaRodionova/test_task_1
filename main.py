import textract

file_name = "test_file.pdf"


def read_file(file_name):
    file_data = textract.process(file_name, method='pdfminer')
    parse_file_data = str(file_data).split('\\n')
    result = {}
    for elem in parse_file_data:
        if ":" in elem:
            colon_index = elem.find(":")
            key = elem[0:colon_index].strip()
            value = elem[colon_index + 1:len(elem)].strip()
            result[key] = value
    return result


read_file(file_name)
