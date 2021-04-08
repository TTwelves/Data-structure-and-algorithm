'''
# @Title:
# @Time : 2021/4/8 18:02
# @File : test_a.py.py
# @Software: PyCharm

'''
import pytest


def func1(x):
    x = x * 2
    return x


    # 多组参数
@pytest.mark.parametrize(
        'a,b',
        [
            (1,2),
            (10,20),
            (3,30)
    ]
)
def testcase_01(a,b):
    assert func1(a)==b


# pytest装饰器
@pytest.fixture()
def login():
    username="jack"
    return username


class TestDemo:

    def testcase_01(self,login):
        print(f'a  username={login}')

    def testcase_02(self):
        print('b')

    def testcase_03(self):
        print('c')

if __name__ == '__main__':
    pytest.main(['test_a.py','-v'])
