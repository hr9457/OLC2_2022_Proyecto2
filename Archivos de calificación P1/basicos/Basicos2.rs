fn main(){
    println!("hola mundo!!!!");
    println!((2*1)*3);
    println!(-1+4);
    println!(-2+(4*2)+(10/2));
    println!(-2.5+(4.4*2.1)+(10.5/2.2));

    println!((2*1)*3);
    println!(-1+4);
    println!(-2+(4*2)+(10/2));
    println!(-2.5+(4.4*2.1)+(10.5/2.2));



    println!(true);
    println!(false);
    println!(false || false);
    println!(1>3 || 1>3);

    println!(false && false);
    println!(false && true);
    println!(true && false);
    println!(true && true);


    println!(!true);

    println!(i64::pow(2,2));

    println!(f64::pow(3.3,2.2));
}






fn main() {
    let mut x : i64 = 10;
    let mut a : i64 = 10;
    let mut b : f64 = 10.2;
    let mut c : bool = true;
    let mut d : String = "hello world";


    println!(x);
    println!(a);
    println!(b);
    println!(c);
    println!(d);

    println!(x + a);
    println!("Hello world"<"hola");


    let mut x : i64 = 10;
    let mut a : i64 = 15;

    let mut z = 10;
    let mut a = 4.4;

    println!("{}",z as f64);


    let z : i64 = 33;
    let y : i64 = 55;
    let a : char = 'm';
    println!(z);
    println!("{}",z as f64);
    println!('a');
    println!(a);

    let a = 'm';
    println!(a);


    let mut a : i64 = 15;
    println!(a);
    a = 3;
    println!(a);
}