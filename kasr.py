class Kasr:
    def __init__(self, soorat, makhrag):
        self.soorat = soorat
        self.makhrag = makhrag
    def add(self, kasr2):
        makhrag = self.makhrag * kasr2.makhrag
        soorat = (self.soorat * kasr2.makhrag) + (self.makhrag * kasr2.soorat)
        self.simplify(soorat, makhrag)
    def sub(self, kasr2):
        makhrag = self.makhrag * kasr2.makhrag
        soorat = (self.soorat * kasr2.makhrag) - (self.makhrag * kasr2.soorat)
        self.simplify(soorat, makhrag)
    def mul(self, kasr2):
        makhrag = self.makhrag * kasr2.makhrag
        soorat = self.soorat * kasr2.soorat
        self.simplify(soorat, makhrag)
    def div(self, kasr2):
        makhrag = self.makhrag * kasr2.soorat
        soorat = self.soorat * kasr2.makhrag
        self.simplify(soorat, makhrag)
    def simplify(self, soorat, makhrag):
        if soorat >= makhrag:
            base = soorat / 2
        else:
            base = makhrag / 2
        for i in range(int(base), 1, -1):
            if soorat % i == 0 and makhrag % i == 0:
                soorat /= i
                makhrag /= i
        print(f"Result: {int(soorat)}/{int(makhrag)}")

#////////////////////
# sample output
a = Kasr(1, 2)
b = Kasr(3, 4)
a.add(b)