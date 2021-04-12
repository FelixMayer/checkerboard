from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/')
def welcome():
    return render_template('board_standard.html')

@app.route('/<int:row>')
def squares(row):
    return render_template('board_only_row.html', rows = row)

@app.route('/<int:row>/<int:column>')
def multiply(row, column):
    return render_template('board_change_both.html', rows = row, columns = column)

if __name__=="__main__":  
    app.run(debug=True)