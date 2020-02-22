from src.main.repositories.OperationTableRepository import OperationTableRepository
from src.main.repositories.AccountsTableRepository import AccountTableRepository
from src.main.repositories.TransactionsTableRepository import TransactionsTableRepository
from src.main.resources.CreateTables import CreateTables
import datetime, time


def evenDate1():
    t = datetime.datetime(2017, 4, 5)
    timestamp = time.mktime(t.timetuple())
    return timestamp


def evenDate2():
    t = datetime.datetime(2017, 4, 10)
    timestamp = time.mktime(t.timetuple())
    return timestamp


def evenDate3():
    t = datetime.datetime(2017, 4, 30)
    timestamp = time.mktime(t.timetuple())
    return timestamp


def dueDate1and2():
    t = datetime.datetime(2017, 5, 10)
    timestamp = time.mktime(t.timetuple())
    return timestamp


def dueDate3():
    t = datetime.datetime(2017, 6, 10)
    timestamp = time.mktime(t.timetuple())
    return timestamp


def creatingTables():
    CreateTables.createOperationTypesTable()
    CreateTables.createAccountTable()
    CreateTables.createTransactionTable()


def populatingOperationTable():
    OperationTableRepository().operationTablePopulate(1, 'COMPRA A VISTA', 2)
    OperationTableRepository().operationTablePopulate(2, 'COMPRA PARCELADA', 1)
    OperationTableRepository().operationTablePopulate(3, 'SAQUE', 0)
    OperationTableRepository().operationTablePopulate(4, 'PAGAMENTO', 0)


def populatingAccountTable():
    AccountTableRepository().accountTablePopulate(1, 5000.0, 5000.0)


def populatingTransactionTable():
    TransactionsTableRepository().transactionTablePopulate(1, 1, 1, -50.0, -50.0, evenDate1(), dueDate1and2())
    TransactionsTableRepository().transactionTablePopulate(2, 1, 1, -23.5, -23.5, evenDate2(), dueDate1and2())
    TransactionsTableRepository().transactionTablePopulate(3, 1, 1, -18.7, -18.7, evenDate3(), dueDate3())


creatingTables()
populatingOperationTable()
populatingAccountTable()
populatingTransactionTable()
