#!/usr/bin/env python3
"""Crée la fiche d'un nouvel écran : devices/<CODE>.json

Usage :
  python3 outils/nouvel_ecran.py CM-0002 --agency "Nom agence" --place "Chalet X · Crans"
         [--whatsapp "+41 79 000 00 00"] [--resort crans-montana] [--accent "#c9a96e"] [--lang fr|en|de]
         [--modele CM-0001]

La fiche reprend les services de l'écran modèle (CM-0001 par défaut), à adapter ensuite.
Une fois le fichier publié sur GitHub, l'écran s'installe en tapant le code sur l'iPad.
"""
import argparse, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("code"); ap.add_argument("--agency", default=""); ap.add_argument("--place")
ap.add_argument("--whatsapp"); ap.add_argument("--resort", default="crans-montana")
ap.add_argument("--accent", default=""); ap.add_argument("--lang", default="fr", choices=["fr", "en", "de"])
ap.add_argument("--modele", default="CM-0001")
a = ap.parse_args()
code = re.sub(r"[^A-Z0-9-]", "", a.code.upper())
out = os.path.join(ROOT, "devices", code + ".json")
if os.path.exists(out): sys.exit(f"{out} existe déjà.")
if not os.path.exists(os.path.join(ROOT, "resorts", a.resort + ".json")):
    sys.exit(f"Station inconnue : resorts/{a.resort}.json n'existe pas.")
dev = json.load(open(os.path.join(ROOT, "devices", a.modele + ".json"), encoding="utf-8"))
dev.update({"code": code, "resort": a.resort, "agency": a.agency, "accent": a.accent, "lang": a.lang})
if a.place: dev["place"] = a.place
if a.whatsapp:
    dev["concierge"]["whatsapp"] = a.whatsapp; dev["concierge"]["demo"] = False
json.dump(dev, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"Créé : devices/{code}.json · à publier sur GitHub, puis taper {code} sur l'iPad.")
