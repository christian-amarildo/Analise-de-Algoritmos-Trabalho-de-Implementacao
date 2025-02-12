from collections import defaultdict

gold_medals = defaultdict(int)
silver_medals = defaultdict(int)
bronze_medals = defaultdict(int)

while True:
    try:
        competition = input()
        gold = input()
        silver = input()
        bronze = input()
        
        gold_medals[gold] += 1
        silver_medals[silver] += 1
        bronze_medals[bronze] += 1
    except EOFError:
        break

countries = set(gold_medals.keys()) | set(silver_medals.keys()) | set(bronze_medals.keys())
medal_table = [(country, gold_medals[country], silver_medals[country], bronze_medals[country]) for country in countries]

medal_table.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

print("Quadro de Medalhas")
for country, gold, silver, bronze in medal_table:
    print(country, gold, silver, bronze)
