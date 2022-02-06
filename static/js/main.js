const searchInput = document.getElementById('search-food');
const searchButton = document.getElementById('search-btn')
searchInput.addEventListener('keyup', (e) => {
    e.preventDefault()
    if (e.code !== 'Enter') {
        return 
    }
    const query = e.target.value
    const url = `https://api.calorieninjas.com/v1/nutrition?query=${query}`
    fetch(url,{
        method: 'GET',
        headers: {
            'Content-Type':'application/json',
            'X-Api-Key': 'hiAngQOOJjM3aT18rbLAjg==HNXzumRPD67PiRSd'
        }
    }).then(resp => resp.json())
    .then(console.log)
})

searchButton.addEventListener('click', (e) => {
    const query = searchInput.value;
    const url = `https://api.calorieninjas.com/v1/nutrition?query=${query}`
    fetch(url,{
        method: 'GET',
        headers: {
            'Content-Type':'application/json',
            'X-Api-Key': 'hiAngQOOJjM3aT18rbLAjg==HNXzumRPD67PiRSd'
        }
    }).then(resp => resp.json())
    .then(console.log)
})
