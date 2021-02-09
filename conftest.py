import pytest
import openpyxl
import os
from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application("c:\\Tools\\AddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_xlsx(file):
    wb = openpyxl.load_workbook(os.path.join(os.path.dirname(os.path.realpath(__file__)), "%s.xlsx" % file))
    sheet = wb.worksheets[0]
    excel_list = []
    for row in sheet.rows:
        excel_list.append(row[0].value)
    return excel_list