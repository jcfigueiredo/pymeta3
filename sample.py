from pymeta.runtime import OMetaBase as GrammarBase

class TestGrammar(GrammarBase):
    def rule_dig(self):
        _locals = {self: self}
        self.locals[dig] = _locals
        def _G_or_1():
            _G_exactly_1, lastError = self.exactly(1)
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        def _G_or_2():
            _G_exactly_1, lastError = self.exactly(2)
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        def _G_or_3():
            _G_exactly_1, lastError = self.exactly(3)
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        _G_or_4, lastError = self._or([_G_or_1, _G_or_2, _G_or_3])
        self.considerError(lastError)
        return (_G_or_4, self.currentError)


    def rule_bits(self):
        _locals = {self: self}
        self.locals[bits] = _locals
        def _G_many1_1():
            _G_apply_1, lastError = self._apply(self.rule_dig, "dig", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
        self.considerError(lastError)
        return (_G_many1_2, self.currentError)
