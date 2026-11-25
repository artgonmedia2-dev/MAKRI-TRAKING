"""Génère index.html (version statique pour GitHub Pages) à partir du gabarit Flask.

Le site Flask (app.py, templates/index.html) reste la source unique : après toute
modification du gabarit, relancer :

    python build_static.py

puis commiter index.html. GitHub Pages sert la racine de la branche main.
"""
from pathlib import Path

from flask import render_template

from app import app

PAGES_URL = "https://artgonmedia2-dev.github.io/MAKRI-TRAKING/"


def build() -> Path:
    with app.test_request_context("/"):
        html = render_template("index.html")
    # Liens absolus de Flask (/static/...) -> relatifs, pour l'URL de projet Pages.
    html = html.replace('"/static/', '"static/')
    # og:image doit être une URL absolue publique, pas l'hôte local de rendu.
    html = html.replace("http://localhost/static/", PAGES_URL + "static/")
    out = Path(__file__).with_name("index.html")
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    print(f"Écrit : {build()}")
