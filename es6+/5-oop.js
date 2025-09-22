class Parent{
    constructor(_side1,_side2){
        this.side1 = _side1
        this.side2 = _side2
        console.log(this.side1, this.side2)
    }

    getArea(){
        return this.side1 * this.side2
    }

    set area(value){
        this.side1 = Math.sqrt(value)
        this.side2 = Math.sqrt(value)
    }

    get area(){
        return this.side1 * this.side2
    }

    static meth1(){
        return("Inside static method")
    }
}


// const parent = new Parent(5,6)
// console.log(parent.getArea())
// parent.area = 36
// console.log(parent.area)
// console.log(Parent.meth1())



class Child extends Parent{
    constructor(_val1,_val2){
        super(_val1,_val2)
        console.log("Inside child constructor")
    }
}

// const child = new Child(5,6)


