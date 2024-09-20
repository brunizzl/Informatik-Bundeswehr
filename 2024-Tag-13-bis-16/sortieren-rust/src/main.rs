pub struct Lcg {
    state: u64,
}

impl Lcg {
    pub fn new(seed: u64) -> Self {
        Self { state: seed }
    }

    pub fn next(&mut self) -> u32 {
        let old = self.state;
        //values by Donald Knuth
        self.state = old
            .wrapping_mul(6_364_136_223_846_793_005)
            .wrapping_add(1_442_695_040_888_963_407);
        (old >> 16) as u32 //bits in middle have highest quality
    }

    pub fn next_u64(&mut self) -> u64 {
        let fst_half = self.next() as u64;
        let snd_half = self.next() as u64;
        (fst_half << 32) + snd_half
    }

    pub fn next_in_range(&mut self, a: u64, b: u64) -> u64 {
        (self.next_u64() % (b - a)) + a
    }

    fn zufaellige_liste(&mut self, n: usize) -> Vec<isize> {
        let mut ergebnis = Vec::with_capacity(n);
        for _ in 0..n {
            ergebnis.push(self.next_in_range(0, 2 * n as u64) as isize);
        }
        ergebnis
    }
}

fn mergesort(liste: &[isize]) -> Vec<isize> {
    if liste.len() <= 1 {
        return liste.into();
    }

    let mitte = liste.len() / 2;
    let haelfte_1 = &liste[..mitte];
    let haelfte_2 = &liste[mitte..];

    let sortiert_1 = mergesort(haelfte_1);
    let sortiert_2 = mergesort(haelfte_2);

    let mut ergebnis = Vec::new();

    let mut i1 = 0;
    let mut i2 = 0;
    while i1 < sortiert_1.len() && i2 < sortiert_2.len() {
        if sortiert_1[i1] <= sortiert_2[i2] {
            ergebnis.push(sortiert_1[i1]);
            i1 += 1;
        } else {
            ergebnis.push(sortiert_2[i2]);
            i2 += 1;
        }
    }
    ergebnis.extend_from_slice(&sortiert_1[i1..]);
    ergebnis.extend_from_slice(&sortiert_2[i2..]);

    ergebnis
}

fn mergesort_schnell(liste: &mut [isize]) {
    fn mergesort_mit_speicher(liste: &mut[isize], speicher: &mut[isize]) {
        if liste.len() <= 1 {
            return;
        }
        let mitte = liste.len() / 2;
        let (haelfte_1, haelfte_2) = liste.split_at_mut(mitte);      
        let (sortiert_1, sortiert_2) = speicher.split_at_mut(mitte);  
        mergesort_mit_speicher(haelfte_1, sortiert_1);
        mergesort_mit_speicher(haelfte_2, sortiert_2);
        
        sortiert_1.copy_from_slice(haelfte_1);
        sortiert_2.copy_from_slice(haelfte_2);
        
        let mut i_ergebnis = 0;
        
        let mut i1 = 0;
        let mut i2 = 0;
        while i1 < sortiert_1.len() && i2 < sortiert_2.len() {
            if sortiert_1[i1] <= sortiert_2[i2] {
                liste[i_ergebnis] = sortiert_1[i1];
                i1 += 1;
            } else {
                liste[i_ergebnis] = sortiert_2[i2];
                i2 += 1;
            }
            i_ergebnis += 1;
        }
        let len_1_rest = sortiert_1.len() - i1;
        let len_2_rest = sortiert_2.len() - i2;
        liste[i_ergebnis..(i_ergebnis + len_1_rest)].copy_from_slice(&sortiert_1[i1..]);
        liste[i_ergebnis..(i_ergebnis + len_2_rest)].copy_from_slice(&sortiert_2[i2..]);
    }
    
    let mut speicher = vec![0; liste.len()];
    mergesort_mit_speicher(liste, &mut speicher);
}

fn main() {
    let mut generator = Lcg::new(1);
    for n in 20..80 {
        let laenge = f64::powi(1.2, n) as usize;
        println!("n: {n} laenge: {laenge}");

        println!("mergesort...");
        let mut x = generator.zufaellige_liste(laenge);
        let start_zeit = std::time::Instant::now();
        let sortiert = mergesort(&x);
        let stopp_zeit = std::time::Instant::now();
        println!(
            "fertig: {:?}..{:?} in {} sekunden",
            &sortiert[..5],
            &sortiert[(laenge - 5)..],
            (stopp_zeit - start_zeit).as_secs_f64()
        );
        
        println!("mergesort schnell(er)...");
        let start_zeit = std::time::Instant::now();
        mergesort_schnell(&mut x);
        let stopp_zeit = std::time::Instant::now();
        println!(
            "fertig: {:?}..{:?} in {} sekunden",
            &x[..5],
            &x[(laenge - 5)..],
            (stopp_zeit - start_zeit).as_secs_f64()
        );
        println!();
    }
}

#[cfg(test)]
mod test {

    #[test]
    fn mergesort_test() {
        let unsortiert = vec![2, -5, 3, 5, 9, 20, 2];
        let sortiert = super::mergesort(&unsortiert);
        assert_eq!(&sortiert, &[-5, 2, 2, 3, 5, 9, 20]);
    }
    
    #[test]
    fn mergesort_schnell_test() {
        let mut unsortiert = vec![2, -5, 3, 5, 9, 20, 2];
        super::mergesort_schnell(&mut unsortiert);
        assert_eq!(&unsortiert, &[-5, 2, 2, 3, 5, 9, 20]);
    }
}
