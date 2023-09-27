from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store contributions and groups in memory (in a real app, use a database)
contributions = []
groups = {}

# HTML templates directory
app.template_folder = 'templates'


@app.route('/')
def index():
    return render_template('index.html', group_ids=list(groups.keys()))


@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    if request.method == 'POST':
        group_id = request.form['group_id']
        groups[group_id] = {'contributors': 0, 'total_raised': 0}
    return render_template('create_group.html')


@app.route('/record_contribution', methods=['GET', 'POST'])
def record_contribution():
    if request.method == 'POST':
        email = request.form['email']
        amount = float(request.form['amount'])
        group_id = request.form['group_id']

        if group_id not in groups:
            return "Group not found"

        groups[group_id]['contributors'] += 1
        groups[group_id]['total_raised'] += amount

        contributions.append({'email': email, 'amount': amount, 'group_id': group_id})

    return render_template('record_contribution.html', group_ids=list(groups.keys()))


@app.route('/stats', methods=['GET', 'POST'])
def stats():
    if request.method == 'POST':
        group_id = request.form['group_id']

        if group_id not in groups:
            return "Group not found"

        group_stats = groups[group_id]
        return render_template('stats.html', group_stats=group_stats)

    return render_template('stats.html')


@app.route('/contribution_list', methods=['GET'])
def contribution_list():
    return jsonify(contributions)


if __name__ == '__main__':
    app.run(debug=True)
