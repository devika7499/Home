from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import sqlite3

def get_production_data(request):
    well_api = request.GET.get("well")

    conn = sqlite3.connect("production.db")
    cursor = conn.cursor()

    # Retrieve the annual data for the given well API
    cursor.execute("SELECT OIL, GAS, BRINE FROM production WHERE API_WELL_NUMBER = ?", (well_api,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return JsonResponse({"error": "Well not found"}, status=404)

    oil, gas, brine = row
    return JsonResponse({"oil": oil, "gas": gas, "brine": brine})
