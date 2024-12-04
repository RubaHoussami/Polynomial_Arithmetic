import pytest
from flask import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("data, expected_result", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A', 'hex2': '002B'}, {'hex': '0x0031', 'bin': '0b0000000000110001'}),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '0000000000101011'}, {'hex': '0x0031', 'bin': '0b0000000000110001'})
])
def test_add_endpoint(client, data, expected_result):
    response = client.post('/add', json=data)
    print(response.json)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert data['result']['hex'] == expected_result['hex']
    assert data['result']['bin'] == expected_result['bin']

@pytest.mark.parametrize("data, expected_result", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A', 'hex2': '002B'}, {'hex': '0x0031', 'bin': '0b0000000000110001'}),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '0000000000101011'}, {'hex': '0x0031', 'bin': '0b0000000000110001'})
])
def test_subtract_endpoint(client, data, expected_result):
    response = client.post('/subtract', json=data)
    print(response.json)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert data['result']['hex'] == expected_result['hex']
    assert data['result']['bin'] == expected_result['bin']

@pytest.mark.parametrize("data, expected_result", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A', 'hex2': '002B'}, {'hex': '0x0093', 'bin': '0b0000000010010011'}),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '0000000000101011'}, {'hex': '0x0093', 'bin': '0b0000000010010011'})
])
def test_multiply_endpoint(client, data, expected_result):
    response = client.post('/multiply', json=data)
    print(response.json)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert data['result']['hex'] == expected_result['hex']
    assert data['result']['bin'] == expected_result['bin']

@pytest.mark.parametrize("data, expected_result", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A', 'hex2': '002B'}, {'quotient_hex': '0x0000', 'remainder_hex': '0x001A', 'quotient_bin': '0b0000000000000000', 'remainder_bin': '0b0000000000011010'}),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '0000000000101011'}, {'quotient_hex': '0x0000', 'remainder_hex': '0x001A', 'quotient_bin': '0b0000000000000000', 'remainder_bin': '0b0000000000011010'})
])
def test_divide_endpoint(client, data, expected_result):
    response = client.post('/divide', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'quotient_hex' in data
    assert 'remainder_hex' in data
    assert 'quotient_bin' in data
    assert 'remainder_bin' in data
    assert data['quotient_hex'] == expected_result['quotient_hex']
    assert data['remainder_hex'] == expected_result['remainder_hex']
    assert data['quotient_bin'] == expected_result['quotient_bin']
    assert data['remainder_bin'] == expected_result['remainder_bin']

@pytest.mark.parametrize("data, expected_result", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex': '001A'}, {'hex': '0x001A', 'bin': '0b0000000000011010'}),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin': '0000000000011010'}, {'hex': '0x001A', 'bin': '0b0000000000011010'})
])
def test_modulo_endpoint(client, data, expected_result):
    response = client.post('/modulo', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert 'hex' in data['result']
    assert 'bin' in data['result']
    assert data['result']['hex'] == expected_result['hex']
    assert data['result']['bin'] == expected_result['bin']

@pytest.mark.parametrize("data, expected_result", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex': '001A'}, {'hex': '0x00FD', 'bin': '0b0000000011111101'}),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin': '0000000000011010'}, {'hex': '0x00FD', 'bin': '0b0000000011111101'})
])
def test_invert_endpoint(client, data, expected_result):
    response = client.post('/invert', json=data)
    print(response.json)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'result' in data
    assert 'hex' in data['result']
    assert 'bin' in data['result']
    assert data['result']['hex'] == expected_result['hex']
    assert data['result']['bin'] == expected_result['bin']

@pytest.mark.parametrize("data", [
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010'},
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '00ZZ', 'hex2': '002B'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '002B'}
])
def test_add_endpoint_failure(client, data):
    response = client.post('/add', json=data)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

@pytest.mark.parametrize("data", [
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010'},
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '00ZZ', 'hex2': '002B'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '002B'},
])
def test_subtract_endpoint_failure(client, data):
    response = client.post('/subtract', json=data)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

@pytest.mark.parametrize("data", [
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010'},
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '00ZZ', 'hex2': '002B'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '002B'}
])
def test_multiply_endpoint_failure(client, data):
    response = client.post('/multiply', json=data)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

@pytest.mark.parametrize("data, expected_status", [
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '00ZZ', 'hex2': '002B'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '002B'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex1': '001A', 'hex2': '0000'}, 404),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin1': '0000000000011010', 'bin2': '0000000000000000'}, 404)
])
def test_divide_endpoint_failure(client, data, expected_status):
    response = client.post('/divide', json=data)
    assert response.status_code == expected_status
    data = json.loads(response.data)
    assert 'error' in data

@pytest.mark.parametrize("data", [
    {'m': 8, 'bits': 16, 'type': 'hex'},
    {'m': 8, 'bits': 16, 'type': 'bin'},
    {'m': 8, 'bits': 16, 'type': 'hex', 'hex': '00ZZ'},
    {'m': 8, 'bits': 16, 'type': 'bin', 'bin': '002B'},
])
def test_modulo_endpoint_failure(client, data):
    response = client.post('/modulo', json=data)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

@pytest.mark.parametrize("data, expected_status", [
    ({'m': 8, 'bits': 16, 'type': 'hex'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'bin'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex': '00ZZ'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin': '002B'}, 400),
    ({'m': 8, 'bits': 16, 'type': 'hex', 'hex': '0000'}, 404),
    ({'m': 8, 'bits': 16, 'type': 'bin', 'bin': '0000000000000000'}, 404)
])
def test_invert_endpoint_failure(client, data, expected_status):
    response = client.post('/invert', json=data)
    assert response.status_code == expected_status
    data = json.loads(response.data)
    assert 'error' in data
