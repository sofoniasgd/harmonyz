from flask import Flask, jsonify, request, render_template_string, redirect, url_for
import random
import json
import os
from datetime import datetime

app = Flask(__name__)

# Configuration file path
CONFIG_FILE = 'config.json'

# Default configuration
DEFAULT_CONFIG = {
    'locations': [
        {'name': 'New York', 'lat': 40.7128, 'lng': -74.0060, 'country': 'USA'},
        {'name': 'London', 'lat': 51.5074, 'lng': -0.1278, 'country': 'UK'},
        {'name': 'Tokyo', 'lat': 35.6762, 'lng': 139.6503, 'country': 'Japan'},
        {'name': 'Sydney', 'lat': -33.8688, 'lng': 151.2093, 'country': 'Australia'},
        {'name': 'Paris', 'lat': 48.8566, 'lng': 2.3522, 'country': 'France'}
    ],
    'response_format': 'detailed',  # 'simple' or 'detailed'
    'include_timestamp': True,
    'max_locations_per_request': 10
}

def load_config():
    """Load configuration from file or create default"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            return DEFAULT_CONFIG.copy()
    return DEFAULT_CONFIG.copy()

def save_config(config):
    """Save configuration to file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def generate_random_location_data(count=1, config=None):
    """Generate random location data based on configuration"""
    if config is None:
        config = load_config()
    
    locations = config.get('locations', DEFAULT_CONFIG['locations'])
    response_format = config.get('response_format', 'detailed')
    include_timestamp = config.get('include_timestamp', True)
    
    results = []
    
    for _ in range(min(count, config.get('max_locations_per_request', 10))):
        base_location = random.choice(locations)
        
        # Add some randomness to coordinates (within ~10km radius)
        lat_offset = random.uniform(-0.1, 0.1)
        lng_offset = random.uniform(-0.1, 0.1)
        
        location_data = {
            'latitude': round(base_location['lat'] + lat_offset, 6),
            'longitude': round(base_location['lng'] + lng_offset, 6),
        }
        
        if response_format == 'detailed':
            location_data.update({
                'city': base_location['name'],
                'country': base_location['country'],
                'accuracy': random.randint(5, 50),  # meters
                'altitude': random.randint(0, 500)  # meters
            })
        
        if include_timestamp:
            location_data['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        
        results.append(location_data)
    
    return results

# API Endpoints
@app.route('/api/location', methods=['GET'])
def get_single_location():
    """API endpoint to get a single random location"""
    try:
        config = load_config()
        location_data = generate_random_location_data(1, config)[0]
        
        return jsonify({
            'status': 'success',
            'data': location_data
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/locations', methods=['GET'])
def get_multiple_locations():
    """API endpoint to get multiple random locations"""
    try:
        config = load_config()
        count = request.args.get('count', 5, type=int)
        
        # Limit count based on configuration
        max_count = config.get('max_locations_per_request', 10)
        count = min(count, max_count)
        
        location_data = generate_random_location_data(count, config)
        
        return jsonify({
            'status': 'success',
            'count': len(location_data),
            'data': location_data
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Configuration Web Interface
@app.route('/')
def config_page():
    """Configuration page"""
    config = load_config()
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Location API Configuration</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input, select, textarea { width: 100%; padding: 8px; margin-bottom: 10px; }
            button { background: #007cba; color: white; padding: 10px 20px; border: none; cursor: pointer; }
            button:hover { background: #005a87; }
            .location-item { border: 1px solid #ddd; padding: 10px; margin: 5px 0; }
            .api-info { background: #f5f5f5; padding: 15px; margin: 20px 0; }
            .remove-btn { background: #dc3545; color: white; padding: 5px 10px; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Location API Server Configuration</h1>
        
        <div class="api-info">
            <h3>API Endpoints:</h3>
            <p><strong>Single Location:</strong> GET /api/location</p>
            <p><strong>Multiple Locations:</strong> GET /api/locations?count=5</p>
        </div>
        
        <form method="POST" action="/update-config">
            <div class="form-group">
                <label>Response Format:</label>
                <select name="response_format">
                    <option value="simple" {{ 'selected' if config.response_format == 'simple' else '' }}>Simple (lat/lng only)</option>
                    <option value="detailed" {{ 'selected' if config.response_format == 'detailed' else '' }}>Detailed (with city, country, etc.)</option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Include Timestamp:</label>
                <select name="include_timestamp">
                    <option value="true" {{ 'selected' if config.include_timestamp else '' }}>Yes</option>
                    <option value="false" {{ 'selected' if not config.include_timestamp else '' }}>No</option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Max Locations Per Request:</label>
                <input type="number" name="max_locations_per_request" value="{{ config.max_locations_per_request }}" min="1" max="100">
            </div>
            
            <h3>Base Locations</h3>
            <div id="locations">
                {% for i, location in enumerate(config.locations) %}
                <div class="location-item">
                    <input type="text" name="location_name_{{ i }}" placeholder="City Name" value="{{ location.name }}">
                    <input type="number" name="location_lat_{{ i }}" placeholder="Latitude" value="{{ location.lat }}" step="any">
                    <input type="number" name="location_lng_{{ i }}" placeholder="Longitude" value="{{ location.lng }}" step="any">
                    <input type="text" name="location_country_{{ i }}" placeholder="Country" value="{{ location.country }}">
                    <button type="button" class="remove-btn" onclick="removeLocation(this)">Remove</button>
                </div>
                {% endfor %}
            </div>
            
            <button type="button" onclick="addLocation()">Add Location</button>
            <br><br>
            
            <button type="submit">Save Configuration</button>
        </form>
        
        <script>
            let locationCount = {{ config.locations|length }};
            
            function addLocation() {
                const locationsDiv = document.getElementById('locations');
                const locationItem = document.createElement('div');
                locationItem.className = 'location-item';
                locationItem.innerHTML = `
                    <input type="text" name="location_name_${locationCount}" placeholder="City Name">
                    <input type="number" name="location_lat_${locationCount}" placeholder="Latitude" step="any">
                    <input type="number" name="location_lng_${locationCount}" placeholder="Longitude" step="any">
                    <input type="text" name="location_country_${locationCount}" placeholder="Country">
                    <button type="button" class="remove-btn" onclick="removeLocation(this)">Remove</button>
                `;
                locationsDiv.appendChild(locationItem);
                locationCount++;
            }
            
            function removeLocation(button) {
                button.parentElement.remove();
            }
        </script>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, config=config, enumerate=enumerate)

@app.route('/update-config', methods=['POST'])
def update_config():
    """Update configuration from form submission"""
    try:
        config = load_config()
        
        # Update basic settings
        config['response_format'] = request.form.get('response_format', 'detailed')
        config['include_timestamp'] = request.form.get('include_timestamp') == 'true'
        config['max_locations_per_request'] = int(request.form.get('max_locations_per_request', 10))
        
        # Update locations
        locations = []
        i = 0
        while f'location_name_{i}' in request.form:
            name = request.form.get(f'location_name_{i}')
            lat = request.form.get(f'location_lat_{i}')
            lng = request.form.get(f'location_lng_{i}')
            country = request.form.get(f'location_country_{i}')
            
            if name and lat and lng and country:
                locations.append({
                    'name': name,
                    'lat': float(lat),
                    'lng': float(lng),
                    'country': country
                })
            i += 1
        
        if locations:
            config['locations'] = locations
        
        save_config(config)
        return redirect(url_for('config_page'))
    
    except Exception as e:
        return f"Error updating configuration: {str(e)}", 500

if __name__ == '__main__':
    print("Starting Location API Server...")
    print("Configuration page: http://localhost:5000")
    print("API endpoints:")
    print("  - Single location: http://localhost:5000/api/location")
    print("  - Multiple locations: http://localhost:5000/api/locations?count=5")
    app.run(debug=True, host='0.0.0.0', port=5000)
