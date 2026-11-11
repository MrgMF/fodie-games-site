#!/usr/bin/env python3
"""Generate the static legal pages (FR + EN). Run: python3 tools/gen_legal.py
Output is committed; Cloudflare Pages needs no build. Placeholders {{EDITEUR_*}} stay
in the HTML until replaced (see URLS.md)."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATE = {"fr": "11 novembre 2026", "en": "November 11, 2026"}
DEL_MAIL = "lufygate@gmail.com"

def mail(lang):
    subj = {"fr": "Suppression de compte Cryptorche", "en": "Cryptorche account deletion"}[lang]
    body = {"fr": "Identifiant de compte (affiche dans le jeu) : ", "en": "Account ID (shown in the game): "}[lang]
    from urllib.parse import quote
    return f"mailto:{DEL_MAIL}?subject={quote(subj)}&body={quote(body)}"

# ---------------------------------------------------------------- pages (fr, en)
PAGES = {}

PAGES["privacy"] = {
 "fr": ("cryptorche/confidentialite", "Politique de confidentialité de Cryptorche", """
<p>Responsable du traitement : {{EDITEUR_RAISON_SOCIALE}}, {{EDITEUR_ADRESSE}}, <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a> (voir les <a href="/mentions-legales">mentions légales</a>).</p>
<h2>En bref</h2>
<p>Cryptorche est un jeu mobile gratuit, sans publicité. La version hors ligne n'envoie rien. La version avec services crée automatiquement un <strong>compte anonyme</strong> : nous ne demandons ni nom, ni e-mail, ni numéro de téléphone, ni localisation, ni accès aux contacts.</p>
<h2>Données traitées</h2>
<div class="tw"><table>
<thead><tr><th scope="col">Donnée</th><th scope="col">Finalité</th><th scope="col">Base légale (RGPD)</th><th scope="col">Durée</th></tr></thead>
<tbody>
<tr><td>Progression et réglages, stockés sur l'appareil</td><td>Jouer</td><td>Contrat (6.1.b)</td><td>Jusqu'à la désinstallation</td></tr>
<tr><td>Identifiant de compte et secret d'appareil (générés au hasard), solde de gemmes, inventaire, quêtes et passe, plafond de dépense mensuel, résumés de parties</td><td>Fournir le compte, sauvegarder et rétablir vos achats, calculer les récompenses, éviter la triche</td><td>Contrat (6.1.b)</td><td>Durée du compte ; suppression sous 30 jours après la demande ; suppression automatique après 24 mois d'inactivité</td></tr>
<tr><td>Justificatifs d'achat Google Play (identifiant de transaction, produit, montant, date)</td><td>Livrer l'achat, comptabilité, litiges</td><td>Contrat (6.1.b) et obligation légale (6.1.c)</td><td>10 ans (art. L123-22 du Code de commerce)</td></tr>
<tr><td>Journaux techniques (adresse IP, erreurs)</td><td>Sécurité, diagnostic, lutte contre la fraude</td><td>Intérêt légitime (6.1.f)</td><td>12 mois maximum</td></tr>
<tr><td>Messages envoyés au support</td><td>Répondre</td><td>Intérêt légitime / contrat</td><td>3 ans après le dernier échange</td></tr>
</tbody></table></div>
<p>Nous n'utilisons <strong>aucune publicité</strong>, aucun outil de mesure d'audience, aucun profilage commercial et ne vendons aucune donnée. Les données de jeu sont transmises en HTTPS uniquement.</p>
<h2>Destinataires et sous-traitants</h2>
<ul>
<li><strong>Oracle Cloud Infrastructure</strong>, région Paris (France) : hébergement du serveur de jeu et des journaux.</li>
<li><strong>Google</strong> (Google Play, Google Payments) : distribution de l'application et paiement. Google paie et nous transmet un justificatif d'achat, jamais vos données bancaires. Les politiques de Google s'appliquent à ce traitement.</li>
<li><strong>Cloudflare</strong> : hébergement de ce site statique et DNS. Il voit votre adresse IP lorsque vous consultez ces pages ; aucun cookie n'est déposé.</li>
<li><strong>OVH</strong> : bureau d'enregistrement du nom de domaine.</li>
</ul>
<h2>Transferts hors Union européenne</h2>
<p>Le serveur de jeu est situé dans l'Union européenne. Google et Cloudflare peuvent traiter des données aux États-Unis ; ces transferts reposent sur le Data Privacy Framework ou sur des clauses contractuelles types (art. 44 à 46 du RGPD).</p>
<h2>Cookies et traceurs</h2>
<p>Le jeu n'utilise ni cookie ni identifiant publicitaire. L'identifiant de compte et le secret d'appareil, strictement nécessaires au fonctionnement du compte, sont conservés chiffrés sur votre appareil. Ce site n'utilise aucun cookie, aucun outil de mesure et aucun script externe.</p>
<h2>Mineurs</h2>
<p>En dessous de 15 ans, l'accord d'un parent ou représentant légal est nécessaire pour utiliser un service en ligne (art. 45 de la loi Informatique et Libertés). Les achats sont réservés aux majeurs ou aux mineurs autorisés par leur représentant légal. Un parent peut demander la suppression du compte de son enfant par les moyens de la <a href="/cryptorche/suppression-compte">page de suppression de compte</a>.</p>
<h2>Vos droits</h2>
<p>Accès, rectification, effacement, limitation, opposition, portabilité (art. 15 à 22 du RGPD), et directives sur le sort de vos données après décès. Pour supprimer votre compte, suivez la <a href="/cryptorche/suppression-compte">page dédiée</a>. Pour les autres droits, écrivez à <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a> en indiquant votre identifiant de compte ; nous répondons sous un mois. En cas de désaccord, vous pouvez saisir la <a href="https://www.cnil.fr/fr/plaintes">CNIL</a>.</p>
<h2>Modifications</h2>
<p>Si nous ajoutons un outil de mesure ou un rapport d'incidents, cette page sera mise à jour et nommera le prestataire avant son activation.</p>
"""),
 "en": ("en/cryptorche/privacy", "Cryptorche Privacy Policy", """
<p>Data controller: {{EDITEUR_RAISON_SOCIALE}}, {{EDITEUR_ADRESSE}}, <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a> (see the <a href="/en/legal-notice">legal notice</a>).</p>
<h2>Summary</h2>
<p>Cryptorche is a free mobile game with no ads. The offline version sends nothing. The version with online services automatically creates an <strong>anonymous account</strong>: we never ask for your name, email, phone number or location, and never access your contacts.</p>
<h2>Data we process</h2>
<div class="tw"><table>
<thead><tr><th scope="col">Data</th><th scope="col">Purpose</th><th scope="col">Legal basis (GDPR)</th><th scope="col">Retention</th></tr></thead>
<tbody>
<tr><td>Progress and settings, stored on your device</td><td>Playing the game</td><td>Contract (6.1.b)</td><td>Until you uninstall</td></tr>
<tr><td>Account ID and device secret (randomly generated), gem balance, inventory, quests and pass, monthly spending cap, match summaries</td><td>Provide the account, back up and restore purchases, compute rewards, prevent cheating</td><td>Contract (6.1.b)</td><td>Life of the account; deleted within 30 days of a request; automatically deleted after 24 months of inactivity</td></tr>
<tr><td>Google Play purchase records (transaction ID, product, amount, date)</td><td>Deliver purchases, accounting, disputes</td><td>Contract (6.1.b) and legal obligation (6.1.c)</td><td>10 years (French Commercial Code, art. L123-22)</td></tr>
<tr><td>Technical logs (IP address, errors)</td><td>Security, diagnostics, fraud prevention</td><td>Legitimate interest (6.1.f)</td><td>12 months maximum</td></tr>
<tr><td>Messages sent to support</td><td>Reply</td><td>Legitimate interest / contract</td><td>3 years after the last exchange</td></tr>
</tbody></table></div>
<p>We use <strong>no advertising</strong>, no analytics, no commercial profiling, and we do not sell data. Game data is sent over HTTPS only.</p>
<h2>Recipients and processors</h2>
<ul>
<li><strong>Oracle Cloud Infrastructure</strong>, Paris (France) region: hosts the game server and logs.</li>
<li><strong>Google</strong> (Google Play, Google Payments): app distribution and payment. Google handles payment and gives us a purchase record, never your card details. Google's own policies apply.</li>
<li><strong>Cloudflare</strong>: hosts this static website and DNS. It sees your IP address when you visit these pages; no cookie is set.</li>
<li><strong>OVH</strong>: domain name registrar.</li>
</ul>
<h2>Transfers outside the European Union</h2>
<p>The game server is in the European Union. Google and Cloudflare may process data in the United States; such transfers rely on the Data Privacy Framework or standard contractual clauses (GDPR art. 44 to 46).</p>
<h2>Cookies and trackers</h2>
<p>The game uses no cookie and no advertising ID. The account ID and device secret, strictly necessary for the account to work, are stored encrypted on your device. This website uses no cookie, no analytics and no external script.</p>
<h2>Minors</h2>
<p>Under 15 (France), a parent or legal guardian's consent is required to use an online service. Purchases are for adults or minors authorised by their guardian. A parent may request deletion of their child's account through the <a href="/en/cryptorche/delete-account">account deletion page</a>.</p>
<h2>Your rights</h2>
<p>Access, rectification, erasure, restriction, objection and portability (GDPR art. 15 to 22). To delete your account, follow the <a href="/en/cryptorche/delete-account">dedicated page</a>. For other rights, email <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a> with your account ID; we reply within one month. You may also lodge a complaint with your data protection authority (in France, the <a href="https://www.cnil.fr/en/complaints">CNIL</a>).</p>
<h2>Changes</h2>
<p>If we add analytics or crash reporting, this page will be updated and name the provider before it is switched on.</p>
"""),
}

PAGES["delete"] = {
 "fr": ("cryptorche/suppression-compte", "Supprimer mon compte Cryptorche", """
<p>Vous pouvez supprimer votre compte Cryptorche et les données associées à tout moment, gratuitement. Application : <strong>Cryptorche</strong>, développeur : <strong>Marega Studio</strong>.</p>
<h2>Dans le jeu (recommandé)</h2>
<ol>
<li>Ouvrez Cryptorche, puis <strong>Réglages → Supprimer le compte</strong>.</li>
<li>Confirmez deux fois (double confirmation : l'action est définitive).</li>
</ol>
<p>Le compte est supprimé côté serveur immédiatement ; les éventuelles copies de sauvegarde sont purgées sous <strong>30 jours</strong> au plus. Les gemmes non dépensées sont perdues.</p>
<h2>Sans le jeu (désinstallé ou inaccessible)</h2>
<p>Envoyez-nous votre demande avec l'<strong>identifiant de compte</strong>, affiché dans le jeu (Réglages → Compte). Sans cet identifiant, nous ne pouvons pas retrouver un compte anonyme.</p>
<p><a class="btn" href="__MAILTO__">Envoyer la demande par e-mail</a></p>
<p>Ou écrivez à <a href="mailto:__DEL__">__DEL__</a> avec pour objet « Suppression de compte Cryptorche ». Nous pouvons demander une preuve simple que le compte est le vôtre. Nous traitons la demande sous <strong>30 jours</strong> au plus.</p>
<h2>Ce qui est supprimé</h2>
<ul>
<li>Le compte (identifiant, secret d'appareil) ;</li>
<li>la sauvegarde en ligne : solde de gemmes, inventaire, quêtes, passe, plafond de dépense, résumés de parties ;</li>
<li>les journaux techniques liés au compte (purge automatique à 12 mois).</li>
</ul>
<h2>Ce qui est conservé, et pourquoi</h2>
<ul>
<li>Les <strong>justificatifs d'achat</strong> (identifiant de transaction, montant, date) sont conservés <strong>10 ans</strong> pour nos obligations légales comptables (art. L123-22 du Code de commerce), sans lien avec votre profil de jeu une fois le compte supprimé.</li>
<li>Google Play conserve ses propres données d'achat selon ses règles.</li>
</ul>
<h2>Mineurs et autres droits</h2>
<p>Un parent ou représentant légal peut demander la suppression du compte d'un enfant par le même moyen. Autres droits (accès, portabilité…) : voir la <a href="/cryptorche/confidentialite">politique de confidentialité</a>.</p>
"""),
 "en": ("en/cryptorche/delete-account", "Delete my Cryptorche account", """
<p>You can delete your Cryptorche account and associated data at any time, free of charge. App: <strong>Cryptorche</strong>, developer: <strong>Marega Studio</strong>.</p>
<h2>In the game (recommended)</h2>
<ol>
<li>Open Cryptorche, then <strong>Settings → Delete account</strong>.</li>
<li>Confirm twice (double confirmation: the action is permanent).</li>
</ol>
<p>The account is deleted on the server immediately; any backup copies are purged within <strong>30 days</strong>. Unspent gems are lost.</p>
<h2>Without the game (uninstalled or inaccessible)</h2>
<p>Send us your request with the <strong>account ID</strong> shown in the game (Settings → Account). Without it, we cannot locate an anonymous account.</p>
<p><a class="btn" href="__MAILTO__">Send the request by email</a></p>
<p>Or write to <a href="mailto:__DEL__">__DEL__</a> with the subject "Cryptorche account deletion". We may ask for simple proof that the account is yours. We process requests within <strong>30 days</strong>.</p>
<h2>What is deleted</h2>
<ul>
<li>The account (ID, device secret);</li>
<li>the online save: gem balance, inventory, quests, pass, spending cap, match summaries;</li>
<li>technical logs tied to the account (automatically purged after 12 months).</li>
</ul>
<h2>What is kept, and why</h2>
<ul>
<li><strong>Purchase records</strong> (transaction ID, amount, date) are kept <strong>10 years</strong> to meet our statutory accounting obligations (French Commercial Code, art. L123-22), unlinked from your game profile once the account is deleted.</li>
<li>Google Play keeps its own purchase data under its own rules.</li>
</ul>
<h2>Minors and other rights</h2>
<p>A parent or legal guardian may request deletion of a child's account the same way. Other rights (access, portability...): see the <a href="/en/cryptorche/privacy">privacy policy</a>.</p>
"""),
}

PAGES["legal"] = {
 "fr": ("mentions-legales", "Mentions légales", """
<p>Informations fournies en application de l'article 6, III de la loi n° 2004-575 du 21 juin 2004 (LCEN).</p>
<h2>Éditeur</h2>
<p>{{EDITEUR_RAISON_SOCIALE}} (nom commercial : Marega Studio), {{EDITEUR_FORME}}<br>
SIRET : {{EDITEUR_SIRET}}<br>
Adresse : {{EDITEUR_ADRESSE}}<br>
Contact : <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a><br>
TVA : {{EDITEUR_TVA}}<br>
Directeur de la publication : {{EDITEUR_DIRECTEUR_PUBLICATION}}</p>
<h2>Hébergement</h2>
<ul>
<li>Site web : <strong>Cloudflare, Inc.</strong>, 101 Townsend St, San Francisco, CA 94107, États-Unis.</li>
<li>Serveur de jeu : <strong>Oracle Cloud Infrastructure</strong>, région Paris (France).</li>
<li>Nom de domaine : <strong>OVH SAS</strong>, 2 rue Kellermann, 59100 Roubaix, France.</li>
</ul>
<h2>Propriété intellectuelle</h2>
<p>Les textes, images, sons, personnages, code et interfaces de Cryptorche sont protégés par le Code de la propriété intellectuelle. Les éléments tiers sont utilisés sous leur licence d'origine. Toute reproduction sans autorisation écrite est interdite, hors exceptions légales.</p>
<h2>Signalement d'un contenu</h2>
<p>Pour signaler un contenu illicite, écrivez à <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a> en indiquant l'emplacement du contenu et vos motifs (règlement (UE) 2022/2065, art. 16 ; LCEN art. 6, I, 5).</p>
<h2>Données personnelles</h2>
<p>Voir la <a href="/cryptorche/confidentialite">politique de confidentialité</a> et la <a href="/cryptorche/suppression-compte">suppression de compte</a>. Ce site n'utilise aucun cookie, aucun outil de mesure et aucun script externe.</p>
"""),
 "en": ("en/legal-notice", "Legal notice", """
<p>Information provided under article 6, III of French law no. 2004-575 of 21 June 2004 (LCEN).</p>
<h2>Publisher</h2>
<p>{{EDITEUR_RAISON_SOCIALE}} (trade name: Marega Studio), {{EDITEUR_FORME}}<br>
SIRET: {{EDITEUR_SIRET}}<br>
Address: {{EDITEUR_ADRESSE}}<br>
Contact: <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a><br>
VAT: {{EDITEUR_TVA}}<br>
Publication director: {{EDITEUR_DIRECTEUR_PUBLICATION}}</p>
<h2>Hosting</h2>
<ul>
<li>Website: <strong>Cloudflare, Inc.</strong>, 101 Townsend St, San Francisco, CA 94107, USA.</li>
<li>Game server: <strong>Oracle Cloud Infrastructure</strong>, Paris (France) region.</li>
<li>Domain name: <strong>OVH SAS</strong>, 2 rue Kellermann, 59100 Roubaix, France.</li>
</ul>
<h2>Intellectual property</h2>
<p>The texts, images, sounds, characters, code and interfaces of Cryptorche are protected by intellectual property law. Third-party elements are used under their original licences. Reproduction without written permission is prohibited except where the law allows.</p>
<h2>Reporting content</h2>
<p>To report illegal content, email <a href="mailto:{{EDITEUR_EMAIL}}">{{EDITEUR_EMAIL}}</a> with the location of the content and your reasons (Regulation (EU) 2022/2065, art. 16).</p>
<h2>Personal data</h2>
<p>See the <a href="/en/cryptorche/privacy">privacy policy</a> and <a href="/en/cryptorche/delete-account">account deletion</a>. This website uses no cookie, no analytics and no external script.</p>
"""),
}

LABELS = {
 "fr": dict(skip="Aller au contenu", nav=[("/cryptorche/confidentialite", "Confidentialité"), ("/cryptorche/suppression-compte", "Suppression de compte"), ("/mentions-legales", "Mentions légales")], upd="Dernière mise à jour", other="English"),
 "en": dict(skip="Skip to content", nav=[("/en/cryptorche/privacy", "Privacy"), ("/en/cryptorche/delete-account", "Delete account"), ("/en/legal-notice", "Legal notice")], upd="Last updated", other="Français"),
}

def write(lang, slug, title, body, other_slug):
    L = LABELS[lang]
    body = body.replace("__MAILTO__", mail(lang).replace("&", "&amp;")).replace("__DEL__", DEL_MAIL)
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h.strip("/") == slug else ""}>{t}</a>' for h, t in L["nav"])
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="robots" content="index,follow">
<title>{title} - Marega Studio</title>
<link rel="alternate" hreflang="{'en' if lang=='fr' else 'fr'}" href="/{other_slug}">
<link rel="stylesheet" href="/legal.css">
</head>
<body>
<a class="skip" href="#main">{L['skip']}</a>
<header><div class="w"><b>Marega Studio</b><nav aria-label="Navigation">{nav}<a lang="{'en' if lang=='fr' else 'fr'}" href="/{other_slug}">{L['other']}</a></nav></div></header>
<main id="main" class="w">
<h1>{title}</h1>
<p class="meta">{L['upd']} : {DATE[lang]}</p>
{body}
</main>
<footer><div class="w">&copy; 2026 Marega Studio</div></footer>
</body>
</html>
"""
    out = ROOT / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

for key, v in PAGES.items():
    write("fr", *v["fr"], other_slug=v["en"][0])
    write("en", *v["en"], other_slug=v["fr"][0])
print("ok")
