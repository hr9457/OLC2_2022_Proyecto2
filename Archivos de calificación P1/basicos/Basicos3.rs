
fn main() {
    let a:i64 = 100;
    let b:i64 = 100;
    let c:i64 = 7;
    let f:bool = true;
    let j:f64 = 10.0;
    let k:f64 = 10.0;

    println!("");
    println!("");
    if a > b || b < c {
        println!(">>>>>> Esto no debería de imprimirse");
    }else{
        println!(">>>>>> Esto debería de imprimirse");
    }



    if a == b && j == k || 14 != c {
        println!(">>>>>> Esto debería de imprimirse");
    }else{
        println!(">>>>>> Esto no debería de imprimirse");
    }


    let val1:i64 = 5;
    let resp:i64 = 5;
    let mut valorVerdadero : i64 = 100;




    if((valorVerdadero == (50 + 50 + (val1 - val1))) && ! ! ! ! ! ! ! ! ! ! true) {
        println!(">>>>>> En este lugar deberia de entrar :)");
        valorVerdadero = 50;
    }
    println!(valorVerdadero);
}
