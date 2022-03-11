from requests import get
from bs4 import BeautifulSoup


def getHTML(url):
    response = get(url)
    return response.text


def getSearchKeyWord():
    keyword = input("[+] Enter Search Keyword: ")
    response = getHTML(f"https://www.alldatasheet.com/view.jsp?Searchword={keyword}")
    return response


def getAvailableElectronics(htmlDoc):
    parser = BeautifulSoup(htmlDoc, 'html.parser')
    availableDataSheets = []
    for dataSheetLink in parser.find_all('a'):
        if 'pdf' in dataSheetLink.get('href'):
            availableDataSheets.append(dataSheetLink.get_text())
            print(dataSheetLink.get_text().strip())
    return availableDataSheets


def getDataSheetsLinks(htmlDoc):
    parser = BeautifulSoup(htmlDoc, 'html.parser')
    dataSheetsLinks = []
    for dataSheetLink in parser.find_all('a'):
        if 'pdf' in dataSheetLink.get('href'):
            dataSheetsLinks.append(dataSheetLink.get('href'))
    print(dataSheetsLinks)
    return dataSheetsLinks


def main():
    htmlDoc = getSearchKeyWord()
    availableDataSheets = getAvailableElectronics(htmlDoc)
    dataSheetsLinks = getDataSheetsLinks(htmlDoc)


if __name__ == '__main__':
    main()
