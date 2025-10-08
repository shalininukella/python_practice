from main import weather

def test_weather():
    assert weather(21) == "hot"