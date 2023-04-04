var backpack_api = {
    async get_all_items(character_id) { 
        var items = []
        await fetch(`http://127.0.0.1:5000/api/items/get_all/${character_id}`, {
            method: 'GET',
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        })
        .then(response => {
            // indicates whether the response is successful (status code 200-299) or not
            if (!response.ok) {
                throw new Error(`Request failed with status ${reponse.status}`)
            }
            return response.json()
        })
        .then(data => {
            data.forEach(element => {
                items.push(
                    {
                        id: element["id"],
                        name: element["name"],
                        descr: element["descr"],
                        amount: element["amount"]
                    }
                )
            });
        })
        .catch(error => console.log(error))
        return items;
    }
  }
  
  export default backpack_api