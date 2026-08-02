import pytest
from unittest.mock import patch
from src.services.career_service import CareerService

@patch('src.ats.scorer.calculate_ats_score')
def test_service_evaluate_ats(mock_calculate_ats):
    mock_calculate_ats.return_value = {'score': 85, 'matched_keywords': ['python'], 'missing_keywords': [], 'recommendations': []}
    service = CareerService()
    result = service.evaluate_ats('resume sample', 'job description')
    assert result['score'] == 85
    mock_calculate_ats.assert_called_once_with('resume sample', 'job description')
