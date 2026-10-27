#!/usr/bin/env python3
"""Build the dependency-free, static PoolPilot Pages site from reviewed policy drafts."""

from __future__ import annotations

from html import escape
from pathlib import Path
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {
    "fr": {
        "name": "Français", "home": "Accueil", "privacy": "Confidentialité", "support": "Assistance", "legal": "Mentions légales",
        "tagline": "L’essentiel de votre activité piscine, à portée de main.",
        "intro": "Clients, bassins, interventions et planning réunis dans une expérience pensée pour les professionnels de la piscine.",
        "eyebrow": "L’application iPhone des piscinistes", "view_privacy": "Lire la politique de confidentialité",
        "view_support": "Obtenir de l’aide", "features_title": "Un quotidien plus fluide, du premier rendez-vous au rapport.",
        "features": [
            ("01", "Dossiers clairs", "Retrouvez les clients, les piscines, les équipements et les échéances au même endroit."),
            ("02", "Interventions rapides", "Consignez mesures, produits, tâches et photos au fil de votre visite."),
            ("03", "Planning maîtrisé", "Organisez vos tournées, rendez-vous récurrents et travaux de maintenance."),
            ("04", "Rapports soignés", "Générez des rapports PDF à partir des informations réellement enregistrées."),
        ],
        "privacy_callout_title": "Vos dossiers restent sous votre contrôle.",
        "privacy_callout": "La version 1 auditée conserve les dossiers professionnels localement sur l’appareil. Les exports et sauvegardes sont déclenchés par l’utilisateur. Consultez la politique pour le détail et ses limites.",
        "draft_badge": "Vérification juridique en cours", "draft_text": "Le registre applicable, la situation TVA et la mention du téléphone de l’hébergeur restent à confirmer. Le site est accessible, mais ces points ne sont pas considérés comme validés.",
        "support_intro": "Ressources et repères pour utiliser PoolPilot. L’éditeur répond aux demandes d’assistance par email.",
        "support_cards": [
            ("Dossiers et sauvegardes", "Depuis l’application, conservez une copie de vos données avec l’export de sauvegarde. Gardez l’archive dans un endroit sûr : elle n’est pas chiffrée par PoolPilot."),
            ("Abonnement", "La gestion et la restauration des achats passent par les fonctions Apple disponibles dans les réglages de l’application. Les dossiers existants restent consultables après expiration."),
            ("Photos et rapports", "Les photos ajoutées aux dossiers sont stockées localement. Vérifiez le contenu d’un rapport PDF avant de choisir où le partager."),
        ],
        "support_contact": "Contact d’assistance", "support_contact_intro": "Arnaud Mourcel · EI, micro-entrepreneur · SIREN 883 531 113 · 244 rue de Bègles, 33800 Bordeaux, France.", "support_retention": "Conservation prévue des emails d’assistance : 12 mois après le dernier échange, sous réserve des exceptions décrites dans la politique de confidentialité.",
        "support_note": "Pour une question relative aux données personnelles, consultez aussi la politique de confidentialité.",
        "footer": "PoolPilot · Arnaud Mourcel EI", "skip": "Aller au contenu", "lang_label": "Langue du site",
        "home_title": "PoolPilot — L’app des professionnels de la piscine", "privacy_title": "Politique de confidentialité — PoolPilot", "support_title": "Assistance — PoolPilot", "legal_title": "Mentions légales — PoolPilot",
    },
    "en": {
        "name": "English", "home": "Home", "privacy": "Privacy", "support": "Support", "legal": "Legal notice",
        "tagline": "Your pool service business, in one calm place.",
        "intro": "Clients, pools, service visits and scheduling come together in an experience built for pool professionals.",
        "eyebrow": "The iPhone app for pool professionals", "view_privacy": "Read the privacy policy",
        "view_support": "Get support", "features_title": "A smoother day, from the first appointment to the final report.",
        "features": [
            ("01", "Clear records", "Find customers, pools, equipment and upcoming work together."),
            ("02", "Fast service visits", "Record readings, products, tasks and photos during a visit."),
            ("03", "Organized schedule", "Plan routes, recurring appointments and maintenance work."),
            ("04", "Polished reports", "Generate PDF reports from information actually recorded."),
        ],
        "privacy_callout_title": "Your professional records stay in your hands.",
        "privacy_callout": "The reviewed version 1 stores professional records locally on the device. Users choose when to export or back up data. Read the policy for details and limitations.",
        "draft_badge": "Legal review in progress", "draft_text": "The applicable register, VAT position and hosting-provider telephone notice still need confirmation. This website is accessible, but these points are not considered resolved.",
        "support_intro": "Guidance for using PoolPilot. The publisher responds to support requests by email.",
        "support_cards": [
            ("Records and backups", "Use the app’s backup export to keep a copy of your data. Store the archive securely: PoolPilot does not encrypt it."),
            ("Subscription", "Manage and restore purchases through Apple controls in the app’s settings. Existing records remain available to read after expiry."),
            ("Photos and reports", "Photos added to records are stored locally. Review a PDF report before choosing where to share it."),
        ],
        "support_contact": "Support contact", "support_contact_intro": "Arnaud Mourcel · French sole proprietor and micro-entrepreneur · SIREN 883 531 113 · 244 rue de Bègles, 33800 Bordeaux, France.", "support_retention": "Planned retention of support emails: 12 months after the last exchange, subject to the exceptions explained in the privacy policy.",
        "support_note": "For questions about personal data, also read the privacy policy.",
        "footer": "PoolPilot · Arnaud Mourcel EI", "skip": "Skip to content", "lang_label": "Site language",
        "home_title": "PoolPilot — The app for pool professionals", "privacy_title": "Privacy policy — PoolPilot", "support_title": "Support — PoolPilot", "legal_title": "Legal notice — PoolPilot",
    },
    "es": {
        "name": "Español", "home": "Inicio", "privacy": "Privacidad", "support": "Ayuda", "legal": "Aviso legal",
        "tagline": "Tu trabajo con piscinas, organizado en un solo lugar.",
        "intro": "Clientes, piscinas, intervenciones y agenda en una experiencia creada para los profesionales del mantenimiento de piscinas.",
        "eyebrow": "La app para iPhone de los profesionales de piscinas", "view_privacy": "Leer la política de privacidad",
        "view_support": "Obtener ayuda", "features_title": "Un día más sencillo, de la primera cita al informe final.",
        "features": [
            ("01", "Expedientes claros", "Consulta clientes, piscinas, equipos y próximos trabajos en un mismo lugar."),
            ("02", "Intervenciones ágiles", "Registra mediciones, productos, tareas y fotos durante la visita."),
            ("03", "Agenda organizada", "Planifica recorridos, citas recurrentes y tareas de mantenimiento."),
            ("04", "Informes cuidados", "Genera informes PDF a partir de la información realmente registrada."),
        ],
        "privacy_callout_title": "Tus expedientes profesionales, bajo tu control.",
        "privacy_callout": "La versión 1 revisada guarda los expedientes localmente en el dispositivo. El usuario decide cuándo exportar o guardar copias. Lee la política para conocer los detalles y límites.",
        "draft_badge": "Revisión jurídica en curso", "draft_text": "Quedan por confirmar el registro aplicable, la situación del IVA y la mención del teléfono del proveedor de alojamiento. El sitio es accesible, pero estos puntos no se consideran resueltos.",
        "support_intro": "Orientación para utilizar PoolPilot. El editor responde a las solicitudes de ayuda por correo.",
        "support_cards": [
            ("Expedientes y copias", "Utiliza la exportación de la app para conservar una copia de tus datos. Guarda el archivo de forma segura: PoolPilot no lo cifra."),
            ("Suscripción", "Gestiona y restaura compras mediante las funciones de Apple en los ajustes de la app. Los expedientes existentes siguen disponibles para consulta tras el vencimiento."),
            ("Fotos e informes", "Las fotos añadidas a los expedientes se guardan localmente. Revisa el informe PDF antes de elegir dónde compartirlo."),
        ],
        "support_contact": "Contacto de asistencia", "support_contact_intro": "Arnaud Mourcel · empresario individual y microempresario · SIREN 883 531 113 · 244 rue de Bègles, 33800 Bordeaux, Francia.", "support_retention": "Conservación prevista de los correos de asistencia: 12 meses desde el último intercambio, con las excepciones indicadas en la política de privacidad.",
        "support_note": "Para consultas sobre datos personales, lee también la política de privacidad.",
        "footer": "PoolPilot · Arnaud Mourcel EI", "skip": "Ir al contenido", "lang_label": "Idioma del sitio",
        "home_title": "PoolPilot — La app de los profesionales de piscinas", "privacy_title": "Política de privacidad — PoolPilot", "support_title": "Ayuda — PoolPilot", "legal_title": "Aviso legal — PoolPilot",
    },
}


def page_path(lang: str, page: str) -> Path:
    parts = [] if lang == "fr" else [lang]
    if page != "home":
        parts.append(page)
    return ROOT.joinpath(*parts, "index.html")


def link(from_lang: str, from_page: str, to_lang: str, to_page: str) -> str:
    source = page_path(from_lang, from_page).parent
    target = page_path(to_lang, to_page).parent
    from os.path import relpath
    relative = relpath(target, source)
    return "./" if relative == "." else relative.rstrip("/") + "/"


def inline_md(value: str) -> str:
    value = escape(value)
    def render_link(match: re.Match[str]) -> str:
        label, url = match.groups()
        parsed = urlsplit(url.replace("&amp;", "&"))
        if parsed.scheme != "https" or not parsed.netloc:
            return match.group(0)
        return f'<a href="{url}" rel="noopener noreferrer">{label}</a>'
    value = re.sub(r"\[([^\]]+)\]\((https://[^\s)]+)\)", render_link, value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"`(.+?)`", r"<code>\1</code>", value)
    return value


def render_markdown(source: str) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    in_list = False

    def flush() -> None:
        if paragraph:
            output.append("<p>" + inline_md(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    for raw in source.splitlines():
        line = raw.strip()
        if not line:
            flush()
            if in_list:
                output.append("</ul>")
                in_list = False
        elif line.startswith("# "):
            flush()
            output.append("<h1>" + inline_md(line[2:]) + "</h1>")
        elif line.startswith("## "):
            flush()
            if in_list:
                output.append("</ul>")
                in_list = False
            output.append("<h2>" + inline_md(line[3:]) + "</h2>")
        elif line.startswith("- "):
            flush()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append("<li>" + inline_md(line[2:]) + "</li>")
        else:
            paragraph.append(line)
    flush()
    if in_list:
        output.append("</ul>")
    return "\n".join(output)


def shell(lang: str, page: str, body: str) -> str:
    data = LANGUAGES[lang]
    title = data[f"{page}_title"]
    css = link(lang, page, "fr", "home") + "assets/site.css"
    nav = "".join(
        f'<a href="{link(lang, page, lang, key)}"' +
        (' aria-current="page"' if page == key else "") +
        f'>{escape(data[key])}</a>'
        for key in ("home", "privacy", "support", "legal")
    )
    langs = "".join(
        f'<a lang="{code}" hreflang="{code}" href="{link(lang, page, code, page)}"' +
        (' aria-current="true"' if lang == code else "") +
        f'>{escape(LANGUAGES[code]["name"])}</a>'
        for code in LANGUAGES
    )
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="{link(lang, page, code, page)}">'
        for code in LANGUAGES
    )
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#092c42">
  <meta name="description" content="{escape(data['intro'])}">
  <title>{escape(title)}</title>
  <link rel="icon" href="{link(lang, page, 'fr', 'home')}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{css}">
  {alternates}
</head>
<body>
  <a class="skip-link" href="#content">{escape(data['skip'])}</a>
  <header class="site-header">
    <div class="shell header-inner">
      <a class="brand" href="{link(lang, page, lang, 'home')}" aria-label="PoolPilot — {escape(data['home'])}">
        <span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 36 36"><path d="M4 22c5.4 0 5.4-5 10.8-5s5.4 5 10.8 5 5.4-5 10.4-5M4 29c5.4 0 5.4-5 10.8-5s5.4 5 10.8 5 5.4-5 10.4-5"/></svg></span>
        <span>PoolPilot</span>
      </a>
      <nav class="primary-nav" aria-label="{escape(data['home'])} / {escape(data['privacy'])} / {escape(data['support'])} / {escape(data['legal'])}">{nav}</nav>
      <nav class="language-nav" aria-label="{escape(data['lang_label'])}">{langs}</nav>
    </div>
  </header>
  <main id="content">{body}</main>
  <footer class="site-footer"><div class="shell footer-inner"><span>{escape(data['footer'])}</span><a href="{link(lang, page, lang, 'privacy')}">{escape(data['privacy'])}</a><a href="{link(lang, page, lang, 'support')}">{escape(data['support'])}</a><a href="{link(lang, page, lang, 'legal')}">{escape(data['legal'])}</a></div></footer>
</body>
</html>
'''


def home(lang: str) -> str:
    d = LANGUAGES[lang]
    cards = "".join(f'<article class="feature-card"><span class="feature-number">{n}</span><h3>{escape(t)}</h3><p>{escape(p)}</p></article>' for n, t, p in d["features"])
    return f'''<section class="hero"><div class="shell hero-grid"><div class="hero-copy"><p class="eyebrow"><span class="eyebrow-dot"></span>{escape(d['eyebrow'])}</p><h1>{escape(d['tagline'])}</h1><p class="lead">{escape(d['intro'])}</p><div class="actions"><a class="button button-primary" href="{link(lang, 'home', lang, 'support')}">{escape(d['view_support'])}<span aria-hidden="true">↗</span></a><a class="button button-quiet" href="{link(lang, 'home', lang, 'privacy')}">{escape(d['view_privacy'])}</a></div></div><div class="hero-art" aria-hidden="true"><div class="art-disc art-disc-one"></div><div class="art-disc art-disc-two"></div><div class="art-lines"><span></span><span></span><span></span></div><div class="art-label">POOLPILOT <small>PROFESSIONAL TOOLS</small></div></div></div></section>
<section class="section"><div class="shell"><p class="section-kicker">POOLPILOT</p><h2 class="section-title">{escape(d['features_title'])}</h2><div class="feature-grid">{cards}</div></div></section>
<section class="section section-end"><div class="shell"><div class="callout"><span class="callout-icon" aria-hidden="true">✦</span><div><h2>{escape(d['privacy_callout_title'])}</h2><p>{escape(d['privacy_callout'])}</p></div><a class="text-link" href="{link(lang, 'home', lang, 'privacy')}">{escape(d['view_privacy'])} →</a></div></div></section>'''


def privacy(lang: str) -> str:
    d = LANGUAGES[lang]
    source = (ROOT / "content" / f"PRIVACY_POLICY_{lang.upper()}.md").read_text(encoding="utf-8")
    return f'''<section class="page-top"><div class="shell narrow"><p class="section-kicker">POOLPILOT / {escape(d['privacy'])}</p></div></section><article class="shell narrow policy-content">{render_markdown(source)}</article>'''


def legal(lang: str) -> str:
    d = LANGUAGES[lang]
    source = (ROOT / "content" / f"LEGAL_{lang.upper()}.md").read_text(encoding="utf-8")
    return f'''<section class="page-top"><div class="shell narrow"><p class="section-kicker">POOLPILOT / {escape(d['legal'])}</p><div class="draft-note" role="note"><strong>{escape(d['draft_badge'])}</strong><p>{escape(d['draft_text'])}</p></div></div></section><article class="shell narrow policy-content">{render_markdown(source)}</article>'''


def support(lang: str) -> str:
    d = LANGUAGES[lang]
    cards = "".join(f'<article class="support-card"><h2>{escape(t)}</h2><p>{escape(p)}</p></article>' for t, p in d["support_cards"])
    return f'''<section class="page-top"><div class="shell narrow"><p class="section-kicker">POOLPILOT / {escape(d['support'])}</p><h1 class="page-title">{escape(d['support_title'])}</h1><p class="page-lead">{escape(d['support_intro'])}</p></div></section><section class="section section-tight"><div class="shell narrow"><div class="support-grid">{cards}</div><div class="contact-panel"><span class="contact-symbol" aria-hidden="true">?</span><div><h2>{escape(d['support_contact'])}</h2><p>{escape(d['support_contact_intro'])}</p><p class="contact-links"><a href="mailto:arnaudmourcel47@gmail.com">arnaudmourcel47@gmail.com</a><a href="tel:+33645480203">06 45 48 02 03</a></p><p class="contact-retention">{escape(d['support_retention'])}</p></div></div><p class="support-note">{escape(d['support_note'])} <a href="{link(lang, 'support', lang, 'privacy')}">{escape(d['privacy'])} →</a></p></div></section>'''


def main() -> None:
    for lang in LANGUAGES:
        for page, renderer in (("home", home), ("privacy", privacy), ("support", support), ("legal", legal)):
            target = page_path(lang, page)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(shell(lang, page, renderer(lang)), encoding="utf-8")
    print("Generated 12 localized HTML pages.")


if __name__ == "__main__":
    main()
