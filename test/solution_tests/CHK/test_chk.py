from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('AAAABBCD') == 260

    def test_chk_illegal_input(self):
        assert checkout_solution.checkout('AAAABEECD') == -1
