# Telangana Map Coloring using CSP (33 Districts)

districts = [
    "Adilabad","Bhadradri Kothagudem","Hyderabad","Jagtial","Jangaon",
    "Jayashankar","Jogulamba","Kamareddy","Karimnagar","Khammam",
    "Komaram Bheem","Mahabubabad","Mahabubnagar","Mancherial","Medak",
    "Medchal","Mulugu","Nagarkurnool","Nalgonda","Narayanpet",
    "Nirmal","Nizamabad","Peddapalli","Rajanna Sircilla","Rangareddy",
    "Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy",
    "Warangal Rural","Warangal Urban","Yadadri"
]

neighbors = {
    "Adilabad": ["Komaram Bheem","Nirmal"],
    "Komaram Bheem": ["Adilabad","Mancherial"],
    "Mancherial": ["Komaram Bheem","Peddapalli","Nirmal"],
    "Nirmal": ["Adilabad","Mancherial","Jagtial"],
    "Jagtial": ["Nirmal","Karimnagar","Rajanna Sircilla"],
    "Karimnagar": ["Jagtial","Peddapalli","Warangal Urban"],
    "Peddapalli": ["Mancherial","Karimnagar"],
    "Rajanna Sircilla": ["Jagtial","Siddipet"],
    "Siddipet": ["Rajanna Sircilla","Medak","Jangaon"],
    "Medak": ["Siddipet","Sangareddy"],
    "Sangareddy": ["Medak","Vikarabad","Rangareddy"],
    "Vikarabad": ["Sangareddy","Rangareddy"],
    "Rangareddy": ["Vikarabad","Hyderabad","Medchal"],
    "Hyderabad": ["Rangareddy","Medchal"],
    "Medchal": ["Hyderabad","Rangareddy","Yadadri"],
    "Yadadri": ["Medchal","Jangaon","Nalgonda"],
    "Jangaon": ["Siddipet","Yadadri","Warangal Urban"],
    "Warangal Urban": ["Karimnagar","Jangaon","Warangal Rural"],
    "Warangal Rural": ["Warangal Urban","Mahabubabad"],
    "Mahabubabad": ["Warangal Rural","Mulugu","Khammam"],
    "Mulugu": ["Mahabubabad","Jayashankar"],
    "Jayashankar": ["Mulugu","Bhadradri Kothagudem"],
    "Bhadradri Kothagudem": ["Jayashankar","Khammam"],
    "Khammam": ["Bhadradri Kothagudem","Mahabubabad","Suryapet"],
    "Suryapet": ["Khammam","Nalgonda"],
    "Nalgonda": ["Suryapet","Yadadri","Nagarkurnool"],
    "Nagarkurnool": ["Nalgonda","Mahabubnagar"],
    "Mahabubnagar": ["Nagarkurnool","Jogulamba","Wanaparthy"],
    "Jogulamba": ["Mahabubnagar"],
    "Wanaparthy": ["Mahabubnagar","Narayanpet"],
    "Narayanpet": ["Wanaparthy"],
    "Nizamabad": ["Kamareddy"],
    "Kamareddy": ["Nizamabad","Medak"]
}

colors = ["Red", "Green", "Blue", "Yellow"]

def is_valid(district, color, assignment):
    for neighbor in neighbors.get(district, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for district in districts:
        if district not in assignment:
            for color in colors:
                if is_valid(district, color, assignment):
                    assignment[district] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[district]
            return None

solution = backtrack({})

print("Telangana Map Coloring:")
for d in solution:
    print(f"{d} → {solution[d]}")
