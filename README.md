# Flask Contribution App

A Flask app for managing contributions. Create groups, record and view contributions.

## Prerequisites

- Python (3.x recommended)
- Flask (`pip install flask`)

## Running the App

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/flask-contribution-app.git
   ```

2. Move to the project directory:

   ```bash
   cd flask-contribution-app
   ```

3. Start the Flask server:

   ```bash
   python app.py
   ```

4. Open http://localhost:5000/ in your browser.

## Usage

**Create a Contribution Group**

Click "Create Group" in the menu. Enter a unique group ID and click "Create Group".

**Record a Contribution**

Click "Record Contribution" in the menu. Fill in the email, contribution amount, and group ID. Click "Record Contribution".

**View Contribution Statistics**

Click "Contribution Statistics" in the menu. Enter the group ID and click "Get Statistics". You'll see the number of contributors and total amount raised.

**List Contributions**

Click "Contribution List" in the menu to see a JSON list of all contributions.

## Customization

Modify the HTML templates and CSS styles in the templates directory to customize the app.
