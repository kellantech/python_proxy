from getres import get_res
from flask import Flask, render_template, request
app = Flask('app')

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/search')
def search():
  qu = request.args.get('query')
  if not(qu.startswith('http') or qu.startswith('https')):
    r = get_res("https://supersearchapi.glitch.me/?search=" + qu)
    return render_template('search.html', res=r,url=("https://supersearchapi.glitch.me/?search=" + qu))
  try:
    
    if qu is None:
      return "query parameter required"  
    r = get_res(qu)
    return render_template('search.html', res=r,url=qu)
  except Exception as e:
    return "error: " + str(e)
    

app.run(host='0.0.0.0')

