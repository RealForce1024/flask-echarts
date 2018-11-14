import xlrd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homing():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def home():

    a = xlrd.open_workbook(r'F:\text\chengjlbb.xlsx')
    sheet1 = a.sheet_by_index(0)
    cols = sheet1.col_values(0)[1:]
    cols1 = sheet1.col_values(1)[1:]
    x = request.form.get("luhao", "null")
    m = [cols1[i] for i in range(len(cols)) if cols[i] == x]
    print(m)
    data = list(range(1, len(m) + 1))
    return jsonify(name=m, name1=data)


if __name__ == '__main__':
    app.run(debug=True)
