account_id = '123'


def test_account(client):

    response = client.patch(f'/v1/accounts/{account_id}')

    assert response.is_json is True
    assert response.status_code == 201
