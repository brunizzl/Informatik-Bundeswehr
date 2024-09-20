
def wurzel_bisektionsverfahren(x: float) -> float:
    untere_schranke = 0.0 # ist garantiert höchstens so groß wie wurzel von x
    obere_schranke = x # ist garantiert mindestens so groß wie wurzel von x
    
    # solange der relative unterschied zwischen den schranken zu groß ist, halbieren
    # wir unseren suchraum
    while obere_schranke - untere_schranke > 1e-12:
        print("wurzel", x, "liegt zwischen", untere_schranke, "und", obere_schranke)
        mitte = (obere_schranke + untere_schranke) / 2.0
        if mitte ** 2 < x:
            untere_schranke = mitte
        else:
            obere_schranke = mitte

    return untere_schranke


def wurzel_newtonverfahren(x: float) -> float:
    # ist w die wurzel von x, löst w die gleichung w ** 2 == x,
    # oder äquivalent 0 == w ** 2 - x.
    # deswegen definieren wir f(w) = w ** 2 - x
    # und wollen die positive nullstelle von f finden.
    def f(w: float) -> float:
        return w ** 2 - x
    
    # erste ableitung von f
    def df(w: float) -> float:
        return 2 * w
        
    # eine tangente T von f an der stelle w_i hat die funktionsgleichung
    # T(w) = f(w_i) + (w - w_i) * df(w_i)
    # die aussage T(w) == 0 gilt damit für w == w_i - f(w_i) / df(w_i)
    # wenn f also eine gerade wäre, 
    # ist das w, für das T(w) == 0 ist, die wurzel von x.
    # wir tun jetzt so, als ob f wenigstens "lokal" "ähnlich aussieht" wie T
    # und finden so unsere wurzel.
    w_i = x
    for i in range(10): # gehe maximal 10 schritte
        print("für i =", i, "ist w_i =", w_i)
        # wenn f quasi null ist, ist w_i quasi die wurzel von x
        if abs(f(w_i)) < 1e-12:
            return w_i
        # sonst: tue so, als of f und T das selbe sind und
        # setze w_i zur nullstelle von T
        w_i = w_i - f(w_i) / df(w_i)
        
    return w_i
