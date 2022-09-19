// intercambio 
fn intercambiar(a: [i64], i: usize, j: usize) {
    let aux: i64 = a[i];
    a[i] = a[j];
    a[j] = aux;
}

// algoritmo de intercambio 
fn ordIntercambio(arr: [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    
    while i < (arr.len()) - 1 {
        j = i + 1;
        while j < (arr.len()) {
            if (arr[i]) > (arr[j]) {
                intercambiar(arr, i, j);
            }
            j = j + 1;
        }
        i = i + 1;
    }
}





fn main () {
    
    // Ordenamiento de intercambio
    // entrada: [8, 4, 6, 2]
    // salida: [2, 4, 6, 8]
    
    let mut arr1: [i64; 4] = [8, 4, 6, 2];
    ordIntercambio(arr1);
    println!("{}", arr1);
}
