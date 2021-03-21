function checkDigits(){
    form = document.querySelector('form')
    values = form.querySelectorAll('input[name="examSetting"]');
    const button = document.querySelector('input[type=submit]')
    if (values[1].value < values[2].value){
        values[1].className += ' is-invalid'
        button.disabled = true
    } else {
        values[1].className = 'form-control'
        button.disabled = false
    }
}