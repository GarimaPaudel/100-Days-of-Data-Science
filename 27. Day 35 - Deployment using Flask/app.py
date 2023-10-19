from flask import Flask, render_template, request


from text_summary import summarizer  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        input_text = request.form['input_text']

        
        summary, doc,  doc_len, summarized_len = summarizer(input_text)

        return render_template('index.html', summary=summary, doc_len=doc_len, summarized_len=summarized_len)

if __name__ == '__main__':
    app.run(debug=True)
