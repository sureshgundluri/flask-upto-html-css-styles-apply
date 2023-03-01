from flask import Flask,render_template


AI=Flask(__name__)

@AI.route('/hai/<name>')
def hai(name):
    return f'hai {name}'

@AI.route('/hello')
def hello():
    return 'hello how are you'

@AI.route('/cricket')
def cricket():
    return render_template('first.html',name='Dhoni',Team='Chennai')

if __name__=="__main__":
    AI.run(debug=True)