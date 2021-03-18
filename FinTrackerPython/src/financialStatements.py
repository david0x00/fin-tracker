from PyQt5.QtCore import pyqtSignal, pyqtSlot
import fileFunctions
import tableFunctions
import forms

class BalanceSheet:

    def __init__(self, home_window):
        self.balance_sheet_file = "../FinancialStatements/BalanceSheet/balanceSheet.json"
        self.home_window = home_window

        self.tables = {
            "current assets" : self.home_window.current_assets_table,
            "fixed assets" : self.home_window.fixed_assets_table,
            "short term liabilities" : self.home_window.st_liabilities_table,
            "long term liabilities" : self.home_window.lt_liabilities_table
        }

        self.total_labels = {
            "current assets" : self.home_window.current_assets_label,
            "fixed assets" : self.home_window.fixed_assets_label,
            "short term liabilities" : self.home_window.st_liabilities_label,
            "long term liabilities" : self.home_window.lt_liabilities_label,
            "total assets" : self.home_window.assets_label,
            "total liabilities" : self.home_window.liabilities_label,
            "net worth" : self.home_window.net_worth_label
        }

        self.balance_sheet = fileFunctions.loadJSON(self.balance_sheet_file)
        self.totals = {}
        self.updateTotals()

        self.updateTables()
        self.updateTotalLabels()
    
    def __getitem__(self, key):
        return self.balance_sheet[key]
    
    def updateTotals(self):
        for category in self.balance_sheet.keys():
            self.totals[category] = 0 
            for sub_category in self.balance_sheet[category].keys():
                self.totals[category] += self.balance_sheet[category][sub_category]
        self.totals["total assets"] = self.totalAssets()
        self.totals["total liabilities"] = self.totalLiabilities()
        self.totals["net worth"] = self.netWorth()
    
    def currentAssets(self):
        return self.totals["current assets"]

    def fixedAssets(self):
        return self.totals["fixed assets"]

    def shortTermLiabilities(self):
        return self.totals["short term liabilities"]

    def longTermLiabilities(self):
        return self.totals["long term liabilities"]
    
    def totalAssets(self):
        return self.currentAssets() + self.fixedAssets()

    def totalLiabilities(self):
        return self.shortTermLiabilities() + self.longTermLiabilities()

    def netWorth(self):
        return self.totalAssets() - self.totalLiabilities()
    
    def updateAllInformation(self):
        self.updateTables()
        self.updateTotals()
        self.updateTotalLabels()

    def updateCategoryTable(self, category):
        table = self.tables[category]
        headers = ["sub-category", "total"]
        sub_categories = self.balance_sheet[category]
        tableFunctions.setRowCount(table, len(sub_categories))
        tableFunctions.setColumnCount(table, len(headers))
        tableFunctions.setHeaders(table, headers)
        for row, sub_category in enumerate(sub_categories.keys()):
            value = fileFunctions.formatCurrency(sub_categories[sub_category])
            tableFunctions.setItem(table, row, 0, sub_category)
            tableFunctions.setItem(table, row, 1, value)
        
    def updateTables(self):
        for category in self.tables.keys():
            self.updateCategoryTable(category)
        fileFunctions.writeJSON(self.balance_sheet_file, self.balance_sheet)
    
    def updateTotalLabel(self, category):
        label = self.total_labels[category]
        value = fileFunctions.formatCurrency(self.totals[category])
        label.setText(value)

    def updateTotalLabels(self):
        for category in self.totals.keys():
            self.updateTotalLabel(category)

class IncomeStatement:
    def __init__(self, home_window):
        self.income_statement_file = "../FinancialStatements/IncomeStatement/incomeStatement.json"
        self.home_window = home_window

        self.tables = {
            "revenue" : self.home_window.revenue_table,
            "cogs" : self.home_window.cogs_table,
            "expenses" : self.home_window.expenses_table
        }

        self.total_labels = {
            "revenue" : self.home_window.revenue_label,
            "cogs" : self.home_window.cogs_label,
            "expenses" : self.home_window.expenses_label,
            "gross profit": self.home_window.gross_profit_label,
            "pre tax income" : self.home_window.pre_tax_income_label,
            "total taxes" : self.home_window.total_taxes_label,
            "post tax income" : self.home_window.post_tax_income_label
        }


        self.income_statement = fileFunctions.loadJSON(self.income_statement_file)
        self.totals = {}
        self.updateTotals()

        self.updateTables()
        self.updateTotalLabels()
        self.home_window.tax_rate_label.setText("Total Taxes (" + str(self.taxRate()*100) + "%):")
    
    def __getitem__(self, key):
        return self.income_statement[key]

    def updateTotals(self):
        for category in self.income_statement.keys():
            if category != "taxes":
                self.totals[category] = 0 
                for sub_category in self.income_statement[category].keys():
                    self.totals[category] += self.income_statement[category][sub_category]
        self.totals["gross profit"] = self.grossProfit()
        self.totals["pre tax income"] = self.preTaxIncome()
        self.totals["total taxes"] = self.taxes()
        self.totals["post tax income"] = self.postTaxIncome()

    def revenue(self):
        return self.totals["revenue"]    

    def cogs(self):
        return self.totals["cogs"]    

    def expenses(self):
        return self.totals["expenses"]

    def taxRate(self):
        return self.income_statement["taxes"]["rate"]
    
    def grossProfit(self):
        return self.revenue() - self.cogs()
    
    def preTaxIncome(self):
        return self.grossProfit() - self.expenses()
    
    def taxes(self):
        return self.preTaxIncome() * self.taxRate()
    
    def postTaxIncome(self):
        return self.preTaxIncome() - self.taxes()

    def updateAllInformation(self):
        self.updateTables()
        self.updateTotals()
        self.updateTotalLabels()

    def updateCategoryTable(self, category):
        table = self.tables[category]
        headers = ["item", "total"]
        sub_categories = self.income_statement[category]
        tableFunctions.setRowCount(table, len(sub_categories))
        tableFunctions.setColumnCount(table, len(headers))
        tableFunctions.setHeaders(table, headers)
        for row, sub_category in enumerate(sub_categories.keys()):
            value = fileFunctions.formatCurrency(sub_categories[sub_category])
            tableFunctions.setItem(table, row, 0, sub_category)
            tableFunctions.setItem(table, row, 1, value)
        
    def updateTables(self):
        for category in self.tables.keys():
            self.updateCategoryTable(category)
        fileFunctions.writeJSON(self.income_statement_file, self.income_statement)

    def updateTotalLabel(self, category):
        label = self.total_labels[category]
        value = fileFunctions.formatCurrency(self.totals[category])
        label.setText(value)

    def updateTotalLabels(self):
        for category in self.totals.keys():
            self.updateTotalLabel(category)
        