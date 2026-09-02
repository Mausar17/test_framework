from conftest import user_client


class TestGetUser:
    def test_existing_user_returns_200_and_correct_data(self, user_client):
        response = user_client.get_user(2)

        assert response.status_code == 200
        body = response.json()
        assert body["data"]["id"] == 2
        assert "email" in body["data"]

    def test_get_nonexistent_user_returns_404(self, user_client):
        response = user_client.get_user(99999)

        assert response.status_code == 404

class TestCreateUser:
    def test_create_user_returns_201_and_echoes_data(self, user_client):
        response = user_client.create_user(name = "Marty", job = "SDET")
        assert response.status_code == 201
        body = response.json()
        assert body["name"] == "Marty"
        assert body["job"] == "SDET"
        assert "id" in body

class TestUpdateUser:
    def test_update_user_returns_200_and_correct_data(self, user_client):
        response = user_client.update_user(2, name = "Marty updated", job = "SDET Senior")
        assert response.status_code == 200
        body = response.json()
        assert body["name"] == "Marty updated"

class TestDeleteUser:
    def test_delete_user_returns_204(self, user_client):
        response = user_client.delete_user(2)

        assert response.status_code == 204

