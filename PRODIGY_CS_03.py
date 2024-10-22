import re

def check_password(password):
    """Fonction pour évaluer la force d'un mot de passe"""
    
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Le mot de passe doit contenir au moins 8 caractères")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Le mot de passe doit contenir au moins une lettre majuscule")
    
    # ... (autres conditions similaires)
    
    # Retourner le score et le feedback
    return score, feedback

# Demander à l'utilisateur d'entrer un mot de passe
password = input("Entrez un mot de passe : ")

# Appeler la fonction et stocker les résultats
strength, feedback = check_password(password)

# Afficher les résultats
if strength == 5:
    print("Mot de passe très fort")
elif strength == 4:
    print("Mot de passe fort")
elif strength >= 2:
    print("Mot de passe moyen")
else:
    print("Mot de passe faible")

if feedback:
    print("Suggestions d'amélioration :")
    for message in feedback:
        print(f"- {message}")