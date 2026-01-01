import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-2G1O1PJ;"
        "DATABASE=TML_UTK_ED;"
        "Trusted_Connection=yes;"
    )
    return conn

