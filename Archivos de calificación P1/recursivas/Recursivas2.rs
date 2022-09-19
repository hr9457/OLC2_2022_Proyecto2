
fn arbol(n: i64){
    for i in 0..n {

        let mut output: String = "".to_string();
        for j in 0..(n - i) {
            output = output + " ".to_string();
        }

        for k in 0..i {
            output = output + "* ".to_string();
        }
        println!("{}",output);

    }
}



fn f(n: i64) -> i64 {
    if n < 2 {
        return 1;
    } else {
        return n * f(n - 1);
    }
}




fn ack(m: i64, n: i64) -> i64 {
    if m == 0 {
        return n + 1;
    } else if n == 0 {
        return ack(m - 1, 1);
    } else {
        return ack(m - 1, ack(m, n - 1));
    }
}



fn main() {


    println!("PINTANDO UN ARBOLITO");
    arbol(9);


    println!("--------------------------");
    println!("----ARCHIVO RECURSIVOS----");
    println!("--------------------------");

    


    println!("Factorial de 6 {}",f(6));
    println!("Factorial de 4 {}",f(4));
    println!("Factorial de 3 {}",f(3));
    println!("");

    println!("");
    println!("Ackerman de 3,0 {}",ack(3,0));
    println!("Ackerman de 2,8 {}",ack(2,8));
    println!("Ackerman de 2,1 {}",ack(2,1));
}
