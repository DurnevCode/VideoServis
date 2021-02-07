from app import client
from models import Video



def test_get():
    res = client.get('/tutorials')

    assert res.status_code == 200
    assert len(res.get_json()) == len(Video.query.all())
    assert res.get_json()[0]['id'] == 2


def test_post():
    data = {
        'name': 'Video #3. Unit testing',
        'description': 'Pytest'
    }
    res = client.post('/tutorials', json=data)

    assert res.status_code == 200
    assert res.get_json()['name'] == data['name']

def test_put():
    res = client.put('/tutorials/1', json={'name': 'UPD'})
    
    assert res.status_code == 200
    assert Video.query.get(1).name == 'UPD'


def test_delete():
    res = client.delete('/tutorials/1')
    
    assert res.status_code == 204
    assert Video.query.get(1) is None