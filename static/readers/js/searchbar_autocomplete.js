new Autocomplete('#autocomplete' , {
    search : input => {
        console.log(input);
        const url = 'search/?title=' + input
        return new Promise(resolve =>{
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                resolve(data.data);
            })
        })
    },
    onSubmit : result => {
        console.log(result)
        const url2 = '/readers/home/redirect/filtered/?title=' + result

        fetch(url2, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }).
        then(window.location.href = '/readers/home/filtered/' + result)
    }
})