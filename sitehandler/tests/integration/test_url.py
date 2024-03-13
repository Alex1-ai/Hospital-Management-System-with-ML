from django import urls


from ..test_config import *
import pytest


    

@pytest.mark.parametrize('param',[
    ('homepage'),
    ('aboutpage'),
    ('loginpage'),
    # ('heartdisease'),
    # ('diabetesdisease')
    ('login_admin'),
    ('createaccountpage')
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200



@pytest.mark.parametrize('param',[
    
    ('heartdisease'),
    ('diabetesdisease'),
    ('adminhome'),
    ('adminaddDoctor'),
    ('adminviewDoctor'),
    ('adminaddReceptionist'),
    ('viewappointments'),

    
])
def test_render_302(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 302
