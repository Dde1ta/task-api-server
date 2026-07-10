class TestMath:

    def test_one(self):
        case1 = "Hello"
        assert case1 == "Hello"

    def test_two(self):
        case2 = 4
        assert case2 % 2 == 0

    def test_three(self):
        case3 = "ThisIs Alphanumeric"
        assert case3.isalnum()
