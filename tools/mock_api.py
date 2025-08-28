#!/usr/bin/env python3
import os, json, yaml
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)

class MockAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')

        if len(path_parts) >= 2 and path_parts[0] == 'entities':
            entity_type = path_parts[1]
            self.handle_entity_request(entity_type)
        else:
            self.send_error(404, "Not Found")

    def handle_entity_request(self, entity_type):
        """Handle requests for entity data"""
        try:
            # Load entities configuration
            entities_file = os.path.join(REPO, "_data/yaml/entities.yaml")
            with open(entities_file, 'r', encoding='utf-8') as f:
                entities_config = yaml.safe_load(f)

            if entity_type in entities_config.get('entities', {}):
                # Load CSV data for the entity
                csv_file = os.path.join(REPO, f"_data/csv/{entity_type}.csv")
                if os.path.exists(csv_file):
                    data = self.load_csv_data(csv_file)
                    self.send_json_response(data)
                else:
                    self.send_json_response([])
            else:
                self.send_error(404, f"Entity type '{entity_type}' not found")

        except Exception as e:
            self.send_error(500, str(e))

    def load_csv_data(self, csv_path):
        """Load CSV data as list of dictionaries"""
        import csv
        data = []
        try:
            with open(csv_path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(dict(row))
        except Exception:
            pass
        return data

    def send_json_response(self, data):
        """Send JSON response"""
        response = json.dumps(data, ensure_ascii=False, indent=2)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(response.encode('utf-8')))
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def log_message(self, format, *args):
        """Override to reduce server noise"""
        if "GET /favicon.ico" not in format:
            super().log_message(format, *args)

def run_server(port=8000):
    """Run the mock API server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, MockAPIHandler)
    print(f"Mock API server running on http://localhost:{port}")
    print("Available endpoints:")
    print("  /entities/document - Document entities")
    print("  /entities/package - Package entities")
    print("  /entities/system - System entities")
    print("  /entities/procurement_item - Procurement items")
    print("  /entities/test - Test entities")
    print("  /entities/defect - Defect entities")
    print("\nPress Ctrl+C to stop the server")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.server_close()

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
