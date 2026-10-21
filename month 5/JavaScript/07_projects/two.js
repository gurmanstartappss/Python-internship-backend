const form= document.querySelector('form')

form.addEventListener('submit',function(e){
    e.preventDefault()

    const weight=parseInt(document.querySelector('#weight').value)
    const height=parseInt(document.querySelector('#height').value)

    //checks
    if(height==='' || height<0 || isNaN(height)){
        results.innerHTML ='please give valid height'
    }
    if(weight==='' || weight<0 || isNaN(weight)){
        results.innerHTML ='please give valid weight'
    }
})console.log.target