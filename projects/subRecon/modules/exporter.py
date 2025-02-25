import json;

def save_results(results, filename):
    print(f"[*] Salvando resultados em {filename}")
    with open(filename, "w") as file:
        json.dump(results,file, indent = 4)
