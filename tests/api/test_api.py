import pytest


# Check username removal
@pytest.mark.change
def test_remove_name(user):
   user.name = ''
   assert user.name == ''

# Check name matching
@pytest.mark.check
def test_name(user):
   assert user.name == 'Oleg'

# Check second name matching
@pytest.mark.check
def test_second_name(user):
   assert user.second_name == 'Kolesnyk'


    