from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('AAAABBCD') == 260
