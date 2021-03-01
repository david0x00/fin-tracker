from PyQt5.QtWidgets import QTableWidgetItem

def setHeaders(table, headers):
    table.setHorizontalHeaderLabels(headers)

def setRowCount(table, count):
    table.setRowCount(count)

def setColumnCount(table, count):
    table.setColumnCount(count)

def setItem(table, row, col, item):
    table.setItem(row, col, QTableWidgetItem(item))