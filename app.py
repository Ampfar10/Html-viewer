from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        html_code = request.form['html_code']
        rendered_html = Markup(html_code)
        return render_template('index.html', html_code=html_code, rendered_html=rendered_html)
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on all available network interfaces with port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
