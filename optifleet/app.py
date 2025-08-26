from flask import Flask, jsonify, request, render_template_string, redirect, url_for
import random
import json
import os
from datetime import datetime
import uuid
from functools import wraps

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
    'max_locations_per_request': 10,
    'api_keys': [],
    'plate_mappings': {}  # plate_number -> city_name mapping
}

def load_config():
    """Load configuration from file or create default"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                if 'api_keys' not in config:
                    config['api_keys'] = []
                if 'plate_mappings' not in config:
                    config['plate_mappings'] = {}
                return config
        except:
            return DEFAULT_CONFIG.copy()
    return DEFAULT_CONFIG.copy()

def save_config(config):
    """Save configuration to file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        config = load_config()
        api_key = request.headers.get('X-API-Key') or request.args.get('api_key')
        
        if not api_key:
            return jsonify({
                'status': 'error',
                'message': 'API key required. Provide via X-API-Key header or api_key parameter.'
            }), 401
        
        if api_key not in config.get('api_keys', []):
            return jsonify({
                'status': 'error',
                'message': 'Invalid API key.'
            }), 403
        
        return f(*args, **kwargs)
    return decorated_function

def generate_random_location_data(plate_number=None, count=1, config=None):
    """Generate random location data based on plate number and configuration"""
    if config is None:
        config = load_config()
    
    locations = config.get('locations', DEFAULT_CONFIG['locations'])
    response_format = config.get('response_format', 'detailed')
    include_timestamp = config.get('include_timestamp', True)
    plate_mappings = config.get('plate_mappings', {})
    
    if plate_number and plate_number in plate_mappings:
        city_name = plate_mappings[plate_number]
        base_location = next((loc for loc in locations if loc['name'] == city_name), None)
        if not base_location:
            # Fallback to random if mapped city not found
            base_location = random.choice(locations)
    else:
        base_location = random.choice(locations)
    
    results = []
    
    for _ in range(min(count, config.get('max_locations_per_request', 10))):
        # Add some randomness to coordinates (within ~10km radius)
        lat_offset = random.uniform(-0.1, 0.1)
        lng_offset = random.uniform(-0.1, 0.1)
        
        location_data = {
            'latitude': round(base_location['lat'] + lat_offset, 6),
            'longitude': round(base_location['lng'] + lng_offset, 6),
        }
        
        if plate_number:
            location_data['plate_number'] = plate_number
        
        if response_format == 'detailed':
            location_data.update({
                'city': base_location['name'],
                'country': base_location['country'],
                'accuracy': random.randint(5, 50),  # meters
                'altitude': random.randint(0, 500),  # meters
                'fuel_level': random.randint(0, 100)  # percentage
            })
        
        if include_timestamp:
            location_data['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        
        results.append(location_data)
    
    return results

@app.route('/api/location', methods=['GET'])
@require_api_key
def get_single_location():
    """API endpoint to get a single random location"""
    try:
        config = load_config()
        plate_number = request.args.get('plate_number')
        
        if not plate_number:
            return jsonify({
                'status': 'error',
                'message': 'plate_number parameter is required.'
            }), 400
        
        location_data = generate_random_location_data(plate_number, 1, config)[0]
        
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
@require_api_key
def get_multiple_locations():
    """API endpoint to get multiple random locations"""
    try:
        config = load_config()
        plate_number = request.args.get('plate_number')
        count = request.args.get('count', 5, type=int)
        
        if not plate_number:
            return jsonify({
                'status': 'error',
                'message': 'plate_number parameter is required.'
            }), 400
        
        # Limit count based on configuration
        max_count = config.get('max_locations_per_request', 10)
        count = min(count, max_count)
        
        location_data = generate_random_location_data(plate_number, count, config)
        
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
            body { font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input, select, textarea { width: 100%; padding: 8px; margin-bottom: 10px; box-sizing: border-box; }
            button { background: #007cba; color: white; padding: 10px 20px; border: none; cursor: pointer; margin: 5px; }
            button:hover { background: #005a87; }
            .location-item, .api-key-item, .plate-mapping-item { border: 1px solid #ddd; padding: 10px; margin: 5px 0; }
            .api-info { background: #f5f5f5; padding: 15px; margin: 20px 0; }
            .remove-btn { background: #dc3545; color: white; padding: 5px 10px; border: none; cursor: pointer; }
            .generate-btn { background: #28a745; }
            .section { margin: 30px 0; padding: 20px; border: 2px solid #eee; }
            .api-key { font-family: monospace; background: #f8f9fa; padding: 5px; }
            .two-column { display: flex; gap: 20px; }
            .column { flex: 1; }
        </style>
    </head>
    <body>
        <h1>Location API Server Configuration</h1>
        
        <div class="api-info">
            <h3>API Endpoints (Authentication Required):</h3>
            <p><strong>Single Location:</strong> GET /api/location?plate_number=ABC123&api_key=YOUR_KEY</p>
            <p><strong>Multiple Locations:</strong> GET /api/locations?plate_number=ABC123&count=5&api_key=YOUR_KEY</p>
            <p><strong>Authentication:</strong> Include API key via X-API-Key header or api_key parameter</p>
        </div>
        
        <form method="POST" action="/update-config">
            
            <div class="section">
                <h3>API Keys Management</h3>
                <div id="api-keys">
                    {% for i, api_key in enumerate(config.api_keys) %}
                    <div class="api-key-item">
                        <span class="api-key">{{ api_key }}</span>
                        <button type="button" class="remove-btn" onclick="removeApiKey(this)">Remove</button>
                        <input type="hidden" name="api_key_{{ i }}" value="{{ api_key }}">
                    </div>
                    {% endfor %}
                </div>
                <button type="button" class="generate-btn" onclick="generateApiKey()">Generate New API Key</button>
            </div>
            
            <div class="section">
                <h3>Plate Number Mappings</h3>
                <div id="plate-mappings">
                    {% for plate_number, city_name in config.plate_mappings.items() %}
                    <div class="plate-mapping-item">
                        <div class="two-column">
                            <div class="column">
                                <label>Plate Number:</label>
                                <input type="text" name="plate_number_{{ loop.index0 }}" value="{{ plate_number }}">
                            </div>
                            <div class="column">
                                <label>City:</label>
                                <select name="plate_city_{{ loop.index0 }}">
                                    {% for location in config.locations %}
                                    <option value="{{ location.name }}" {{ 'selected' if location.name == city_name else '' }}>{{ location.name }}</option>
                                    {% endfor %}
                                </select>
                            </div>
                        </div>
                        <button type="button" class="remove-btn" onclick="removePlateMapping(this)">Remove</button>
                    </div>
                    {% endfor %}
                </div>
                <button type="button" onclick="addPlateMapping()">Add Plate Mapping</button>
            </div>
            
            <div class="section">
                <h3>General Settings</h3>
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
            </div>
            
            <div class="section">
                <h3>Base Locations</h3>
                <div id="locations">
                    {% for i, location in enumerate(config.locations) %}
                    <div class="location-item">
                        <div class="two-column">
                            <div class="column">
                                <input type="text" name="location_name_{{ i }}" placeholder="City Name" value="{{ location.name }}">
                                <input type="text" name="location_country_{{ i }}" placeholder="Country" value="{{ location.country }}">
                            </div>
                            <div class="column">
                                <input type="number" name="location_lat_{{ i }}" placeholder="Latitude" value="{{ location.lat }}" step="any">
                                <input type="number" name="location_lng_{{ i }}" placeholder="Longitude" value="{{ location.lng }}" step="any">
                            </div>
                        </div>
                        <button type="button" class="remove-btn" onclick="removeLocation(this)">Remove</button>
                    </div>
                    {% endfor %}
                </div>
                <button type="button" onclick="addLocation()">Add Location</button>
            </div>
            
            <button type="submit">Save Configuration</button>
        </form>
        
        <script>
            let locationCount = {{ config.locations|length }};
            let apiKeyCount = {{ config.api_keys|length }};
            let plateMappingCount = {{ config.plate_mappings|length }};
            
            function generateApiKey() {
                const apiKey = 'key_' + Math.random().toString(36).substr(2, 32);
                const apiKeysDiv = document.getElementById('api-keys');
                const apiKeyItem = document.createElement('div');
                apiKeyItem.className = 'api-key-item';
                apiKeyItem.innerHTML = `
                    <span class="api-key">${apiKey}</span>
                    <button type="button" class="remove-btn" onclick="removeApiKey(this)">Remove</button>
                    <input type="hidden" name="api_key_${apiKeyCount}" value="${apiKey}">
                `;
                apiKeysDiv.appendChild(apiKeyItem);
                apiKeyCount++;
            }
            
            function removeApiKey(button) {
                button.parentElement.remove();
            }
            
            function addPlateMapping() {
                const plateMappingsDiv = document.getElementById('plate-mappings');
                const cities = {{ config.locations|map(attribute='name')|list|tojson }};
                let cityOptions = '';
                cities.forEach(city => {
                    cityOptions += `<option value="${city}">${city}</option>`;
                });
                
                const plateMappingItem = document.createElement('div');
                plateMappingItem.className = 'plate-mapping-item';
                plateMappingItem.innerHTML = `
                    <div class="two-column">
                        <div class="column">
                            <label>Plate Number:</label>
                            <input type="text" name="plate_number_${plateMappingCount}" placeholder="e.g., ABC123">
                        </div>
                        <div class="column">
                            <label>City:</label>
                            <select name="plate_city_${plateMappingCount}">
                                ${cityOptions}
                            </select>
                        </div>
                    </div>
                    <button type="button" class="remove-btn" onclick="removePlateMapping(this)">Remove</button>
                `;
                plateMappingsDiv.appendChild(plateMappingItem);
                plateMappingCount++;
            }
            
            function removePlateMapping(button) {
                button.parentElement.remove();
            }
            
            function addLocation() {
                const locationsDiv = document.getElementById('locations');
                const locationItem = document.createElement('div');
                locationItem.className = 'location-item';
                locationItem.innerHTML = `
                    <div class="two-column">
                        <div class="column">
                            <input type="text" name="location_name_${locationCount}" placeholder="City Name">
                            <input type="text" name="location_country_${locationCount}" placeholder="Country">
                        </div>
                        <div class="column">
                            <input type="number" name="location_lat_${locationCount}" placeholder="Latitude" step="any">
                            <input type="number" name="location_lng_${locationCount}" placeholder="Longitude" step="any">
                        </div>
                    </div>
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
        
        api_keys = []
        i = 0
        while f'api_key_{i}' in request.form:
            api_key = request.form.get(f'api_key_{i}')
            if api_key:
                api_keys.append(api_key)
            i += 1
        config['api_keys'] = api_keys
        
        plate_mappings = {}
        i = 0
        while f'plate_number_{i}' in request.form:
            plate_number = request.form.get(f'plate_number_{i}')
            plate_city = request.form.get(f'plate_city_{i}')
            if plate_number and plate_city:
                plate_mappings[plate_number] = plate_city
            i += 1
        config['plate_mappings'] = plate_mappings
        
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
    print("API endpoints (authentication required):")
    print("  - Single location: http://localhost:5000/api/location?plate_number=ABC123&api_key=YOUR_KEY")
    print("  - Multiple locations: http://localhost:5000/api/locations?plate_number=ABC123&count=5&api_key=YOUR_KEY")
    app.run(debug=True, host='0.0.0.0', port=5000)