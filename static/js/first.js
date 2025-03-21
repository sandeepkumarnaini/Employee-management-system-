function validate(){
    let n1,n2
    n1=document.querySelector('#t1').value
    n2=document.querySelector('#t2').value
    if(n1<0 || n2<0)
        return false
    else
        return true
}