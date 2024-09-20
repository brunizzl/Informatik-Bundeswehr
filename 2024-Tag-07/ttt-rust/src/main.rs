fn baue_spielfeld() -> [&'static str; 9] {
    return ["_"; 9];
}

fn zeige_spielfeld(feld: &[&str; 9]) {
    println!();
    println!("Feld:   Züge:");
    println!("{} {} {}   1 2 3", feld[0], feld[1], feld[2]);
    println!("{} {} {}   4 5 6", feld[3], feld[4], feld[5]);
    println!("{} {} {}   7 8 9", feld[6], feld[7], feld[8]);
}

fn naechster_zug(feld: &[&str; 9]) -> usize {
    loop {
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        if let Ok(i) = input.trim().parse::<usize>() {
            if !(1..=9).contains(&i) {
                println!("Gültig sind Züge von 1 bis 9.");
            } else if feld[i - 1] != "_" {
                println!("Feld schon besetzt.");
            } else {
                return i - 1;
            }
        } else {
            println!("Gültig sind Züge von 1 bis 9.");
        }
    }
}

fn gewonnen(feld: &[&str; 9], spieler: &str) -> bool {
    let alle_besetzt = |a, b, c| {
        return feld[a] == spieler && feld[b] == spieler && feld[c] == spieler;
    };

    // Zeilen
    return alle_besetzt(0, 1, 2) 
        || alle_besetzt(3, 4, 5)
        || alle_besetzt(6, 7, 8)
        // Spalten
        || alle_besetzt(0, 3, 6)
        || alle_besetzt(1, 4, 7)
        || alle_besetzt(2, 5, 8)
        // Diagonalen
        || alle_besetzt(0, 4, 8)
        || alle_besetzt(6, 4, 2);
}

fn spielen() {
    let mut feld = baue_spielfeld();
    loop {
        for spieler in ["X", "O"] {
            zeige_spielfeld(&feld);
            println!("Spieler {spieler} ist am Zug.");
            let i = naechster_zug(&feld);
            feld[i] = spieler;

            if gewonnen(&feld, spieler) {
                println!("Spieler {spieler} hat gewonnen!");
                return;
            }
            if !feld.contains(&"_") {
                println!("Unentschieden!");
                return;
            }
        }
    }
}

fn main() {
    spielen();
}
