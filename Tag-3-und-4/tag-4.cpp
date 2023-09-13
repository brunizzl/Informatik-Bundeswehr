//hier muessen wir sagen, welche Dinge aus c++ wir benutzen moechten
#include <iostream> //Konsolenausgabe (cout)
#include <string> //str in python
#include <vector> //list in python

//Aufgabe 2
std::string float_zu_str(float x) {
    std::string ohne_vorzeichen = std::to_string(std::abs(x));
    std::string vorzeichen;
    if (x < 0) {
        vorzeichen = " - ";
    }
    else {
        vorzeichen = " + ";
    }
    return vorzeichen + ohne_vorzeichen;
}

//Aufgabe 5
std::string poly_zu_str(std::vector<float> const& poly) {
    std::string ergebnis = std::to_string(poly[0]);
    int laenge = poly.size();
    int i = 1;
    while (i < laenge) {
        float koeff = poly[i];
        ergebnis += float_zu_str(koeff);
        ergebnis += " x^" + std::to_string(i);
        i += 1;
    }
    return ergebnis;
}

//Aufgabe 6
float funktionswert(std::vector<float> const& poly, float x) {
    float ergebnis = 0;
    float x_hoch_i = 1;
    int laenge = poly.size();
    int i = 0;
    while (i < laenge) {
        float koeff = poly[i];
        ergebnis += koeff * x_hoch_i;
        x_hoch_i *= x;
        i += 1;
    }
    return ergebnis;
}

//Aufgabe 7
std::vector<float> ableitung(std::vector<float> const& poly) {
    int laenge = poly.size();
    int i = 1; //beachte: i = 0 wird uebersprungen!
    std::vector<float> ergebnis = std::vector<float>(laenge - 1);
    while (i < laenge) {
        ergebnis[i - 1] = i * poly[i];
        i += 1;
    }
    return ergebnis;
}

//Aufgabe 8
std::vector<float> integral(std::vector<float> const& poly) {
    int laenge = poly.size();
    int i = 0;
    std::vector<float> ergebnis = std::vector<float>(laenge + 1);
    while (i < laenge) {
        float koeff = poly[i];
        ergebnis[i + 1] = koeff / (i + 1);
        i += 1;
    }
    return ergebnis;
}

//diese Funktion wird ausgefehrt, wenn das Programm gestartet wird (als einzige)
int main() {
    std::vector<float> poly = { 3.0, -2.0, 0.0, 0.1 };
    std::cout << "original:  f(x)  = " << poly_zu_str(poly) << "\n";
    
    std::vector<float> abl = ableitung(poly);
    std::cout << "ableitung: f'(x) = " << poly_zu_str(abl) << "\n";
    
    std::vector<float> inte = integral(abl);
    std::cout << "zurueck:   f(x)  = " << poly_zu_str(inte) << "\n";
    
    std::cout << "\n";
    float f_von_1 = funktionswert(poly, 1.0);
    std::cout << "funktionswert: f(1) = " << f_von_1 << "\n";
}



