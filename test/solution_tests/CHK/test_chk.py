from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('AAAABBCD') == 260

    def test_chk_promoEB(self):
        assert checkout_solution.checkout('AAAABBCDEE') == 325

    def test_chk_promo9A(self):
        assert checkout_solution.checkout('AAAAAAAAABBCDEE') == 525

    def test_chk_promo_newF(self):
        assert checkout_solution.checkout('AAAAAAAAABBCDEEFFFF') == 555

    def test_chk_promo_random(self):
        assert checkout_solution.checkout('AAAAAAAAABBCDEEFFFFZZHHHHH') == 700

    def test_chk_illegal_input(self):
        assert checkout_solution.checkout('AAAAB4ZCD') == -1
