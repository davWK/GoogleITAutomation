import csv
data = [{"nom":"Nom", "Contry":"Pays", "Role":"Poste"},{"nom":"David", "Contry":"Worlwide", "Role":"Sr Cloud Architect"},{"nom":"James", "Contry":"US", "Role":"DevOps"},{"nom":"Kaity", "Contry":"UK", "Role":"SWE"},{"nom":"Mays", "Contry":"Ghana", "Role":"Data Scientist"}]
keys = ["nom", "Contry", "Role"]
with open("/home/david/github/By_me/data/IT_People.csv", "w") as stat:
    writer = csv.DictWriter(stat, fieldnames=keys)
    writer.writerows(data)
