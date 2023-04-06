var consumable_api = {

    async get_all_consumables(character_id) { 
        var consumables = []
        await fetch(`/api/consumables/get_all/${character_id}`, {
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
                consumables.push(
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
        return consumables;
    }
  }
  
  export default consumable_api