from flask import Flask, render_template, request
from markupsafe import escape
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log to file the request and response of calling search4letters."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, sep='|', file=log)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Return html result of calling search4letters."""
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def search4web() -> 'html':
    """Return html form to call search4letters."""
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web')


@app.route('/viewlog')
def view_log() -> 'html':
    """Return html table of records from the vsearch.log file."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form parameters', 'Remote_addr', 'User_agent', 'Results')     
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
