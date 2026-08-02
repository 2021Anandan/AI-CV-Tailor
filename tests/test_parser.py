import pytest
from src.services.career_service import CareerService

def test_parse_invalid_extension():
    service = CareerService()
    with pytest.raises(ValueError):
        service.parse_resume('dummy_path.txt')
