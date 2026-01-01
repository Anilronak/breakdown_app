from flask import Flask, render_template, request, redirect
from db import get_connection

def export_excel():
    return "Export route working"



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("add_breakdown.html")

@app.route("/add", methods=["POST"])
def add_breakdown():
    data = request.form
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO breakdown_log
    (breakdown_date, shop_name, machine_name, problem,
     action_taken, attended_by, spare_used, root_cause,
     start_time_new, end_time_new)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    data["date"], data["shop"], data["machine"], data["problem"],
    data["action"], data["attended_by"], data["spare"],
    data["root_cause"], data["start_time_new"], data["end_time_new"])

    conn.commit()
    conn.close()
    return redirect("/history")

@app.route("/history")
def history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *, DATEDIFF(MINUTE, start_time, end_time) AS down_time
        FROM breakdown_log
        ORDER BY breakdown_date DESC
    """)
    records = cursor.fetchall()
    conn.close()
    return render_template("history.html", records=records)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)



