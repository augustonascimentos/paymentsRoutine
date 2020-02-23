from src.main.repositories.OperationTableRepository import OperationTableRepository
from src.main.repositories.AccountsTableRepository import AccountTableRepository
from src.main.repositories.TransactionsTableRepository import TransactionsTableRepository
from src.main.resources.CreateTables import CreateTables
import datetime, time
from decimal import Decimal


class Initialize:

    @staticmethod
    def evenDate1():
        t = datetime.datetime(2017, 4, 5)
        timestamp = time.mktime(t.timetuple())
        return int(timestamp)

    @staticmethod
    def evenDate2():
        t = datetime.datetime(2017, 4, 10)
        timestamp = time.mktime(t.timetuple())
        return int(timestamp)

    @staticmethod
    def evenDate3():
        t = datetime.datetime(2017, 4, 30)
        timestamp = time.mktime(t.timetuple())
        return int(timestamp)

    @staticmethod
    def dueDate1and2():
        t = datetime.datetime(2017, 5, 10)
        timestamp = time.mktime(t.timetuple())
        return int(timestamp)

    @staticmethod
    def dueDate3():
        t = datetime.datetime(2017, 6, 10)
        timestamp = time.mktime(t.timetuple())
        return int(timestamp)

    @staticmethod
    def creatingTables():
        CreateTables.createOperationTypesTable()
        CreateTables.createAccountTable()
        CreateTables.createTransactionTable()

    @staticmethod
    def populatingOperationTable():
        OperationTableRepository().operationTablePopulate(1, 'COMPRA A VISTA', 2)
        OperationTableRepository().operationTablePopulate(2, 'COMPRA PARCELADA', 1)
        OperationTableRepository().operationTablePopulate(3, 'SAQUE', 0)
        OperationTableRepository().operationTablePopulate(4, 'PAGAMENTO', 0)

    @staticmethod
    def populatingAccountTable():
        AccountTableRepository().accountTablePopulate(1, Decimal(5000.0), Decimal(5000.0))

    @staticmethod
    def populatingTransactionTable():
        TransactionsTableRepository().transactionTablePopulate(1, 1, 1,
                                                               round(Decimal(-50.0), 2),
                                                               round(Decimal(-50.0), 2),
                                                               Initialize.evenDate1(),
                                                               Initialize.dueDate1and2())
        TransactionsTableRepository().transactionTablePopulate(2, 1, 1,
                                                               round(Decimal(-23.5), 2),
                                                               round(Decimal(-23.5), 2),
                                                               Initialize.evenDate2(),
                                                               Initialize.dueDate1and2())
        TransactionsTableRepository().transactionTablePopulate(3, 1, 1,
                                                               round(Decimal(-18.7), 2),
                                                               round(Decimal(-18.7), 2),
                                                               Initialize.evenDate3(),
                                                               Initialize.dueDate3())


Initialize.creatingTables()
Initialize.populatingOperationTable()
Initialize.populatingAccountTable()
Initialize.populatingTransactionTable()
