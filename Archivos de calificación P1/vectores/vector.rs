
// PILA
fn pila_vacia(vec: &mut Vec<i64>) -> bool {
    return (vec.len()) == 0;
}


fn apilar(capacidad: usize, vec: &mut Vec<i64>, value: i64) {
    if ((vec.len()) < capacidad) {
        vec.insert(vec.len(), value);
    } else {
        println!("La pila ha llegado a su maxima capacidad");
    }
}


fn desapilar(vec: &mut Vec<i64>) -> i64 {
    if !pila_vacia(vec) {
        return vec.remove(vec.len()-1);
    } else {
        println!("La pila no tiene elementos");
    }
    return 0;
}



// COLA
fn cola_vacia(vec: &mut Vec<i64>) -> bool {
    return vec.len() == 0;
}


fn encolar(capacidad: usize, vec: &mut Vec<i64>, value: i64) {
    if vec.len() < capacidad {
        vec.push(value);
    } else {
        println!("La cola ha llegado a su maxima capacidad");
    }
}


fn desencolar(vec: &mut Vec<i64>) -> i64 {
    if !cola_vacia(vec) {
        return vec.remove(0);
    } else {
        println!("La cola no tiene elementos");
    }
    return 0;
}


fn main() {
    let capacidad: usize = 10;
    let mut pila: Vec<i64> = Vec::with_capacity(capacidad - 2);
    let mut cola: Vec<i64> = Vec![1,2,3,4,5];

    let datos: [i64; 5] = [10,20,30,40,50];

    for dato in datos {
        apilar(capacidad,pila, dato);
    }

    println!("{}", pila);

    println!("{}", desapilar(pila));

    apilar(capacidad,pila, 100);
    apilar(capacidad,pila, 200);
    apilar(capacidad,pila, 300);



    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", desapilar(pila));
    println!("{}", pila);


    println!("Capacidad de pila");
    println!("{}", pila.capacity());
    println!("");


    encolar(capacidad,cola, 800);
    println!("{}", cola);


    println!("{}", desencolar(cola));

    encolar(capacidad,cola, 100);
    encolar(capacidad,cola, 200);
    encolar(capacidad,cola, 300);

    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));
    println!("{}", desencolar(cola));

    println!("{}", cola);
    println!("Capacidad de cola");
    println!("{}", cola.capacity());
    println!("");



    // vectores entre vectores
    let mut lista: Vec<Vec<i64>> = Vec::new();
    
    lista.push(Vec![0; 10]);
    lista.push(Vec![1; 10]);
    lista.push(Vec![2; 10]);
    lista.push(Vec![3; 10]);
    //lista.push(Vec![75,23,10,29,30,12,49,10,93]);


    println!("{}", lista);
    println!("");
    println!("{}", lista[0]);
    println!("{}", lista[1]);
    println!("{}", lista[2]);
    println!("{}", lista[3]);


    let vec = Vec!["Hola", "!", "Sale", "Este", "Semestre", "2022"];
    println!((vec.contains(&"Semestre")) || (vec.contains(&"2023")) );
    println!((vec.contains(&"Semestre")) && (vec.contains(&"2023")) );
    println!( vec.contains(&"Hola") );


}



// /*

// [10, 20, 30, 40, 50]
// 50
// 300
// 200
// 100
// 40
// 30
// 20
// 10
// La pila no tiene elementos
// 0
// []
// Capacidad de pila
// 8

// [1, 2, 3, 4, 5, 800]
// 1
// 2
// 3
// 4
// 5
// 800
// 100
// 200
// 300
// []
// Capacidad de cola
// 10

// [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [75, 23, 10, 29, 30, 12, 49, 10, 93]]

// [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
// [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
// [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
// [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
// [75, 23, 10, 29, 30, 12, 49, 10, 93]
// 93

// true
// false
// true

// */

