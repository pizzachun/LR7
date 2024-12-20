from flask import Flask, render_template
import utils 

app = Flask(__name__)

@app.route('/')
def index():
    try:
       connect = utils.getConnection()
       utils.fillDB(connect)
       result = utils.getResult(connect)
       return render_template('result.html', result = result)
    except Exception as e:
        return '<font color="red"><h1> Ошибка: '+str(e)+'</h1></font>'    
        
    finally:
        utils.closeConnection(connect)

if __name__ == '__main__':
  app.run()