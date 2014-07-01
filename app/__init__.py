from flask import Flask, render_template, request, make_response
from StringIO import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file1 = request.files['file1']
        output_stream = StringIO()
        file1.save(output_stream)
        file2 = request.files['file2']
        file2.save(output_stream)
        print(output_stream.getvalue())
        return output_stream.getvalue()
    else:
        return render_template('upload.html')

@app.route('/download')
def download():
    csv = '''
    name,id
    tom,1
    smith,2
    '''
    response = make_response(csv, 200)
    response.headers['Content-Disposition'] = 'attachment; filename=test.csv'

    return response
