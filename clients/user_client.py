from clients.base_client import BaseClient

class UserClient(BaseClient):
    def get_user(self, user_id):
        return self.get(f'/users/{user_id}')

    def list_users(self, page=1):
        return self.get("/users", params={"page": page})

    def create_user(self, name, job):
        return self.post('/users',json={"name": name, "job": job})

    def update_user(self, user_id, name, job):
        return self.put(f"/users/{user_id}", json={"name": name, "job": job})

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")