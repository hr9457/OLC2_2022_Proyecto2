
fn main() {
    let mut a: i64 = 909;

    println!("=======================================================================");
    println!("==================================IF===================================");
    println!("=======================================================================");

    if (a > 50) {
        println!("IF CORRECTO");
    }else if (a == 56) {
        println!("IF INCORRECTO");
    } else {
        println!("IF INCORRECTO");
    }

    println!("");
    println!("=======================================================================");
    println!("=============================IFs ANIDADOS==============================");
    println!("=======================================================================");
    let aux: i64 = 10;
    if aux > 0 {
        println!("PRIMER IF CORRECTO");
        if true && (aux == 1) {
            println!("SEGUNDO IF INCORRECTO");
        } else if aux > 10 {
            println!("SEGUNDO IF INCORRECTO");
        } else {
            println!("SEGUNDO IF CORRECTO");
        }
    }else if aux <= 3 {
        println!("PRIMER IF INCORRECTO");
        if true && (aux == 1) {
            println!("SEGUNDO IF INCORRECTO");
        } else if aux > 10 {
            println!("SEGUNDO IF INCORRECTO");
        } else {
            println!("SEGUNDO IF CORRECTO");
        } 
    } else if aux == a {
        println!("PRIMER IF INCORRECTO");
        if true && (aux == 1) {
            println!("SEGUNDO IF INCORRECTO");
        } else if aux > 10 {
            println!("SEGUNDO IF INCORRECTO");
        } else {
            println!("SEGUNDO IF CORRECTO");
        } 
    }

    println!("");
    println!("=======================================================================");
    println!("=================================WHILE=================================");
    println!("=======================================================================");

    let mut index: i64 = 0;

    while (index >= 0) {

        if (index == 0) {
            index = index + 100;
        } else if (index > 50) {
            index = index / 2 - 25;
        } else {
            index = (index / 2) - 1;
        } 

        println!(index);
    }

    println!("");
    println!("=======================================================================");
    println!("=============================TRANSFERENCIA=============================");
    println!("=======================================================================");

    a = -1;
    while (a < 5) {
        a = a + 1;
        if a == 3 {
            println!("a");
            continue;
        } else if a == 4 {
            println!("b");
            break;
        } 

        println!("El valor de a es: {}, ", a);
    }

    println!("Se debi?? imprimir");



        for i in 0..9 {

        let mut output: String = "".to_string();
        for j in 0..(10 - i) {
            output = output + " ".to_string();
        }

        for k in 0..i {
            output = output + "* ".to_string();
        }
        println!(output);

    }



}



// ARBOLITO

fn main() {

    for i in 0..9 {

        let mut output: String = "".to_string();
        for j in 0..(10 - i) {
            output = output + " ".to_string();
        }

        for k in 0..i {
            output = output + "* ".to_string();
        }
        println!(output);

    }

}



// RESPUESTA DEL ARCHIVO INTERMEDIO

// =======================================================================
// ==================================IF===================================
// =======================================================================
// IF CORRECTO

// =======================================================================
// =============================IFs ANIDADOS==============================
// =======================================================================
// PRIMER IF CORRECTO
// SEGUNDO IF CORRECTO

// =======================================================================
// =================================WHILE=================================
// =======================================================================
// 100
// 25
// 11
// 4
// 1
// -1

// =======================================================================
// =============================TRANSFERENCIA=============================
// =======================================================================
// El valor de a es: 0, 
// El valor de a es: 1, 
// El valor de a es: 2, 
// a
// b
// Se debi?? imprimir
