
function submit(){
    var em=document.getElementById('em')
    var nm=document.getElementById('nm')
    console.log(em,nm``)
}

function myFunction(val) {
    // debugger;
    var nmreg=/^[\w]{5}$/

    if(nmreg.test(val))
    {
        // console.log('Name valide')
        document.getElementById('error').innerHTML="Name Valide"
        document.getElementById('error').className="text-success"
    }
    else
    {
        // console.log('name not valide')
        document.getElementById('error').innerHTML="Name not Valide"
        document.getElementById('error').className="text-danger"
    }
  }

