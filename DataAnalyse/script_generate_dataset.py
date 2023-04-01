import random
from django.utils import timezone
import csv
from models import Client, CollectData
from job_list import jobs


# Données pour le modèle Client :
for i in range(1000):
    Client.objects.create(
        id=i+1,
        nbr_children=random.randint(0, 5),
        career=random.choice(jobs),
        shopping_price=random.randint(0,1),
    )

# Données pour le modèle CollectData :
for i in range(1000):
    CollectData.objects.create(
        id=i+1,
        cloths = random.randint(20, 250),
        underwear = random.randint(5, 50),
        sportswear = random.randint(45, 300),
        accessories = random.randint(2, 20),
    )

    # Calculer le montant total dépensé pour cette transaction
    shopping_price = cloths + underwear + sportswear + accessories
    Client.objects.update(
        shopping_price=shopping_price,
    )


# Exporter les données pour le modèle Client
with open('DataAnalyse_client.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'nbr_children', 'career', 'shopping_price'])

    for client in Client.objects.all():
        writer.writerow([client.id, client.nbr_children, client.career, client.shopping_price])

# Exporter les données pour le modèle CollectData
with open('DataAnalyse_collectdata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'cloths', 'underwear', 'sportswear', 'accessories'])

    for collect_data in CollectData.objects.all():
        writer.writerow([collect_data.id, collect_data.cloths, collect_data.underwear, collect_data.sportswear, collect_data.accessories])
