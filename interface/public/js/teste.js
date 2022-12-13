// const [button] = document.querySelectorAll("#ok");
// button.addEventListener("click", (e) => {
//     // e.preventDefault();
//     const file = document.getElementById('cpf');
//     const data = new FormData();
//     data.append('cpf', file.files[0])  
//     console.log(file)
//     fetch('http://127.0.0.1:5000/', {
//         method: "POST",
//         body: data, 
//     })
// });

const [button] = document.querySelectorAll("#ok");
button.addEventListener("click", (e) => {
    // e.preventDefault();

    const data = new FormData(document.getElementsByTagName("form")[0]);
    const myheader = {
        'Access-Control-Allow-Origin' : 'http://127.0.0.1:5000/'
    }
  
    fetch('http://127.0.0.1:5000/', {
        method: "POST",
        headers: myheader,
        body: data, 
    })
});
