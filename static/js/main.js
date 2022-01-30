const searchInput = document.getElementById('search-food')
searchInput.addEventListener('keyup', (e) => {
    e.preventDefault()
    console.log(e)
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