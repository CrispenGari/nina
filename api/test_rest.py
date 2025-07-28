class TestREST:
    def test_rest_meta(self):
        from app import app
        import json

        client = app.test_client()
        response = client.get("/")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == {
            "description": "Nice Intelligent Network Assistant (NINA) is a modern customer support chatbot framework powered by AI-driven intent recognition. Nina provides seamless integration through REST and GraphQL APIs, enabling businesses to automate and streamline customer interactions across platforms.",
            "language": "python",
            "libraries": ["pytorch", "googletrans"],
            "main": "Nice Intelligent Network Assistant (NINA)",
            "programmer": "@crispengari",
        }

    def test_rest_ask(self):
        from app import app
        import json

        client = app.test_client()
        response = client.post(
            "/api/v1/ask", json={"message": "Rhoxisa umrhumo wam, nceda."}
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["success"] is True

    def test_rest_ask_with_error(self):
        from app import app
        import json

        client = app.test_client()
        response = client.post("/api/v1/ask")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["success"] is False
        assert data["error"] == "Something went wrong on the server"

    def test_rest_ask_with_no_message(self):
        from app import app
        import json

        client = app.test_client()
        response = client.post("/api/v1/ask", json={})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["success"] is False
        assert (
            data["error"]
            == "You should pass the 'message' in your JSON body while making this request."
        )
