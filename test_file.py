import pytest
from polls.models import Country


@pytest.mark.django_db  # give test access to database
def test_country_create():
    # Create dummy data
    country = Country.objects.create(
      name="Serbia",
      population=6690887,
      area=88499)
    # Assert the dummy data saved as expected
    assert country.name == "Serbia"
    assert country.population == 6690887
