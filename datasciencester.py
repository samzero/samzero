# Python 3.8.0 32 bit

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klei" },
]

friendship_pairs = [(0,1), (0,2), (1,2), (1, 3), (2, 3), (3, 4),
                    (4,5), (5,6), (5,7), (6, 8), (7, 8), (8, 9)]

#inizializza il dict con una lista vuota per ciascun id utente
friendship = {user["id"]: [] for user in users}

# E cicla sulle coppie di amici per popolarlo
for i, j in friendship_pairs:
    friendship[i].append(j)
    friendship[j].append(i)