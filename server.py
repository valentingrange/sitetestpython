from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/about':
            self.path = '/about.html'
        elif self.path == '/jeux-videos/mario-odyssey':
            self.path = '/jeux-videos/mario-odyssey.html'
        elif self.path == '/jeux-videos/zelda-botw':
            self.path = '/jeux-videos/zelda-botw.html'
        elif self.path == '/jeux-videos/zelda-totk':
            self.path = '/jeux-videos/zelda-totk.html'
        elif self.path == '/jeux-videos/minecraft':
            self.path = '/jeux-videos/minecraft.html'

        try:
            content = self.render_template(self.path[1:])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.send_error(404, "File not found")

    def render_template(self, template_name):
        # Charger le fichier de base
        with open('templates/base.html', 'r', encoding='utf-8') as base_file:
            base_content = base_file.read()

        # Charger le menu commun
        with open('templates/menu.html', 'r', encoding='utf-8') as menu_file:
            menu_content = menu_file.read()

        # Charger le contenu spécifique
        with open(f'templates/{template_name}', 'r', encoding='utf-8') as page_file:
            page_content = page_file.read()

        # Insérer le contenu spécifique et le menu dans la base
        base_with_menu = base_content.replace('{{ menu }}', menu_content)
        return base_with_menu.replace('{{ content }}', page_content)

# Configuration du serveur
PORT = 8000
os.chdir(os.path.dirname(__file__))  # Assurez-vous d'être dans le bon dossier

with HTTPServer(('localhost', PORT), MyRequestHandler) as httpd:
    print(f"Server running on http://localhost:{PORT}")
    httpd.serve_forever()
