from app.main import app

def testmain():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 220
    assert response.get_json() == {'message':"Hello World I am Dev Telang!"}
    
    