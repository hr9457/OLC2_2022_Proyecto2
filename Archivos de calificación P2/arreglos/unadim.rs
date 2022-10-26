
fn intercambiar(arr: &mut [i64], i: usize, j: usize) {
    let aux: i64 = a[i];
    a[i] = a[j];
    a[j] = aux;
}


fn ordIntercambio(arr: &mut [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    
    while i < (arr.len() - 1) {
        j = i + 1;

        while j < (arr.len()) {
            if (arr[i]) > (arr[j]) {
                let aux: i64 = arr[i];
                arr[i] = arr[j];
                arr[j] = aux;
            }            
            j = j + 1;
        }


        i = i + 1;
    }

}


fn ordSeleccion(arr2: &mut [i64]) {
    let mut indiceMenor: usize = 0;
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut n: usize = arr2.len();

    while i < (n - 1) {
        ///* comienzo de exploracion indice i */
        indiceMenor = i;

        ///* j explora la sublista */
        j = i + 1;
        while j < n {
            if (arr2[j]) < (arr2[indiceMenor]) {
                indiceMenor = j;
            }
            j = j + 1;
        }

        if i != indiceMenor {
                let aux: i64 = arr2[i];
                arr2[i] = arr2[j];
                arr2[j] = aux;
        }

        i = i + 1;
    }
}



fn ordInsercion(arr3: &mut [i64]) {
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut aux: i64 = 0;

    i = 1;
    while (i < (arr3.len())) {
        j = i;
        aux = arr3[i];

        while j > 0 && aux < (arr3[j-1]) {
            arr3[j] = arr3[j - 1];
            j = j - 1;
        }
        
        arr3[j] = aux;
        i = i + 1;
    }
}








fn main(){

    let mut arr: [i64; 5] = [25, 2, 17, 30, 1];
    ordIntercambio(arr);
	println!(arr);


    let mut arr2: [i64; 10] = [5, 20, 8, 17, 65, 2, 40, 4, 35, 90];
    ordSeleccion(arr2);
    println!(arr2);

}



fn main(){

    let mut arr: [i64; 5] = [25, 2, 17, 30, 1];
    ordIntercambio(arr);
	println!(arr);


    let mut arr2: [i64; 10] = [5, 20, 8, 17, 65, 2, 40, 4, 35, 90];
    ordSeleccion(arr2);
    println!(arr2);


    let mut arr3: [i64; 4] = [90, 3, 40, 10];
    ordInsercion(arr3);
    println!(arr3);

}



fn main(){


    let mut arr3: [i64; 4] = [90, 3, 40, 10];
    ordInsercion(arr3);
    println!(arr3);

}



// RESPUESTA

// [1, 2, 17, 25, 30]
// [2, 4, 5, 8, 17, 20, 35, 40, 65, 90]
// [3, 10, 40, 90]