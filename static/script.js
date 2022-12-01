function getCountry(){
    countryList = ['England', 'Spain', 'France'];
    const index = Math.round(Math.random() * countryList.length);
    const country =  countryList[index - 1];
    const field = document.querySelector('#country');
    field.setAttribute("value", `${country}`);
}