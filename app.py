from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Baca data CSV dari folder static
    df = pd.read_csv('static/data_populasi.csv')

    # Ambil nilai filter dari form
    min_pop = request.form.get('min_pop', '')
    keyword = request.form.get('keyword', '').lower()

    # Filter data berdasarkan input
    filtered_df = df.copy()
    if min_pop:
        filtered_df = filtered_df[filtered_df['populasi'] >= int(min_pop)]
    if keyword:
        filtered_df = filtered_df[filtered_df['nama'].str.lower().str.contains(keyword)]

    # Ubah ke list of dict untuk dikirim ke template
    data = filtered_df.to_dict(orient='records')

    return render_template(
        'home.html',
        data=data,
        min_pop=min_pop,
        keyword=keyword
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
