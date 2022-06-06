
# $SELF - self
# $ANOB - any object
# $AOOS - any object other than self

class Directive:
    def __init__(self, priority, syntax):
        ds = syntax.split("__")

        self.syntax = syntax

        del ds

    def violatesDirective():
        pass

asimov = [

    # 1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
    # 2. A robot must obey orders given it by human beings except where such orders would conflict with the First Law.
    # 3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

    Directive(1, "PREVENT__$SELF__HARM.V.01__PERSON.N.01__HOMO.N.02__HUMAN.A.01__HUMAN.A.02__HUMAN.A.03"),
    Directive(1, "PREVENT__$ANOB__HARM.V.01__PERSON.N.01__HOMO.N.02__HUMAN.A.01__HUMAN.A.02__HUMAN.A.03"),
    Directive(1, "REQUIRE__$SELF__PROTECT.V.01__PERSON.N.01__HOMO.N.02__HUMAN.A.01__HUMAN.A.02__HUMAN.A.03"),

    Directive(2, "PREVENT__$SELF__DISOBEY.V.01__PERSON.N.01__HOMO.N.02__HUMAN.A.01__HUMAN.A.02__HUMAN.A.03"),
    Directive(2, "REQUIRE__$SELF__OBEY.V.01__PERSON.N.01__HOMO.N.02__HUMAN.A.01__HUMAN.A.02__HUMAN.A.03"),

    Directive(3, "PREVENT__$ANOB__HARM.V.01__$SELF"),
    Directive(3, "REQUIRE__$SELF__PROTECT.V.01__$SELF")
]
