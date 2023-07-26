

import pandas as pd
import sqlite3
from sqlite_utils import Database
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods



from django.core.wsgi import get_wsgi_application

from wsgiref.simple_server import make_server

# Step 1: Download the Ohio Quarterly Production Data from the Excel Dataset
df = pd.read_excel('dataset.xls')

# Step 2: Add up the quarterly data to calculate the annual data for oil, gas, and brine for each well based on API WELL NUMBER
df['API WELL  NUMBER'] = df['API WELL  NUMBER'].astype(str)
df['API WELL  NUMBER'] = df['API WELL  NUMBER'].str.replace('.0', '')
annual_data = df.groupby('API WELL  NUMBER')[['OIL', 'GAS', 'BRINE']].sum().to_dict(orient='index')

# Step 3: Using Python, load the calculated annual data into a local SQLite database
conn = sqlite3.connect('annual_data.db')
db = Database(conn)


# Convert annual_data to the correct structure
records = [{"key": key, **values} for key, values in annual_data.items()]

# Create a table to store the annual data
db["annual_data"].upsert_all(records, pk="key")


# Step 4: Make an API using Django to allow for getting the annual data from the database using a GET request
@require_http_methods(['GET'])
def get_annual_data(request):
    api_well_number = request.GET.get('well', '')

    data = db['annual_data'].find_one(key=api_well_number)
    if data is None:
        return JsonResponse({'error': 'No data found for the specified well'}, status=404)

    return JsonResponse(data)

# Step 5: The app should be launchable by running: python main.py
if __name__ == '__main__':
    

    application = get_wsgi_application()
    with make_server('', 8080, application) as server:
        print('Server running on http://localhost:8080...')
        server.serve_forever()


